# """
# Header:
#    This file is a simple example of how to achieve speech to text
# """
#
# import argparse
# import io
# import os
# import speech_recognition as sr
# import whisper
# import torch
# import re
# from datetime import datetime, timedelta
# from queue import Queue
# from tempfile import NamedTemporaryFile
# from sys import platform
# from app.utils.chatgpt_api.chatgpt_api_calls import call_gpt
# import asyncio
# from app.global_code.helpful_functions import create_logger_error, log_it
#
#
# async def main():
#     """
#     ADD CREDIT TO
#     :return:
#     """
#     now = datetime.now()
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--model", default="small", help="Model to use",
#                         choices=["tiny", "base", "small", "medium", "large"])
#     parser.add_argument("--non_english", action='store_false',
#                         help="Don't use the english model.")
#     parser.add_argument("--energy_threshold", default=1000,
#                         help="Energy level for mic to detect.", type=int)
#     parser.add_argument("--record_timeout", default=3,
#                         help="How real time the recording is in seconds.", type=float)
#     parser.add_argument("--phrase_timeout", default=5,
#                         help="How much empty space between recordings before we "
#                              "consider it a new line in the transcription.", type=float)
#     if 'linux' in platform:
#         parser.add_argument("--default_microphone", default='list',
#                             help="Default microphone name for SpeechRecognition. "
#                                  "Run this with 'list' to view available Microphones.", type=str)
#     args = parser.parse_args()
#
#     # The last time a recording was retreived from the queue.
#     phrase_time = None
#     # Current raw audio bytes.
#     last_sample = bytes()
#     # Thread safe Queue for passing data from the threaded recording callback.
#     data_queue = Queue()
#     # We use SpeechRecognizer to record our audio because it has a nice feauture where it can detect when speech ends.
#     recorder = sr.Recognizer()
#     recorder.energy_threshold = args.energy_threshold
#     # Definitely do this, dynamic energy compensation lowers the energy threshold dramtically
#     # to a point where the SpeechRecognizer never stops recording.
#     recorder.dynamic_energy_threshold = False
#
#     # Important for linux users.
#     # Prevents permanent application hang and crash by using the wrong Microphone
#     if 'linux' in platform:
#         mic_name = args.default_microphone
#         if not mic_name or mic_name == 'list':
#             print("Available microphone devices are: ")
#             for index, name in enumerate(sr.Microphone.list_microphone_names()):
#                 print(f"Microphone with name \"{name}\" found")
#             return
#         else:
#             for index, name in enumerate(sr.Microphone.list_microphone_names()):
#                 if mic_name in name:
#                     source = sr.Microphone(sample_rate=16000, device_index=index)
#                     break
#     else:
#         source = sr.Microphone(sample_rate=16000)
#
#     # Load / Download model
#     model = args.model
#     # if args.model != "large" and not args.non_english:
#     model2 = model + ".en"
#     model = PATH_TO_MODEL + model
#     torch.cuda.init()
#     device = 'cuda'
#     audio_model = whisper.load_model(download_root='F:\Coding\Iris_V2\data\models', name=model2).to(device)
#
#     record_timeout = args.record_timeout
#     phrase_timeout = args.phrase_timeout
#
#     temp_file = NamedTemporaryFile().name
#     transcription = ['']
#
#     with source:
#         recorder.adjust_for_ambient_noise(source)
#
#     def record_callback(_, audio: sr.AudioData) -> None:
#         """
#         Threaded callback function to recieve audio data when recordings finish.
#         audio: An AudioData containing the recorded bytes.
#         """
#         # Grab the raw bytes and push it into the thread safe queue.
#         data = audio.get_raw_data()
#         data_queue.put(data)
#
#     # Create a background thread that will pass us raw audio bytes.
#     # We could do this manually but SpeechRecognizer provides a nice helper.
#     recorder.listen_in_background(source, record_callback, phrase_time_limit=record_timeout)
#
#     # Cue the user that we're ready to go.
#     print(f"Model loaded in {datetime.now() - now} seconds. \n")
#
#     logger = create_logger_error(os.path.abspath(__file__), 'main')
#     phrases = []  # list of dictonaries
#     while True:
#         try:
#             # ###################################################################################################
#             now = datetime.utcnow()
#             # Pull raw recorded audio from the queue.
#             if not data_queue.empty():
#                 phrase_complete = False
#                 # If enough time has passed between recordings, consider the phrase complete.
#                 # Clear the current working audio buffer to start over with the new data.
#                 if phrase_time and now - phrase_time > timedelta(seconds=phrase_timeout):
#                     last_sample = bytes()
#                     phrase_complete = True
#                 # This is the last time we received new audio data from the queue.
#                 phrase_time = now
#
#                 # Concatenate our current audio data with the latest audio data.
#                 while not data_queue.empty():
#                     data = data_queue.get()
#                     last_sample += data
#
#                 # Use AudioData to convert the raw data to wav data.
#                 audio_data = sr.AudioData(last_sample, source.SAMPLE_RATE, source.SAMPLE_WIDTH)
#                 wav_data = io.BytesIO(audio_data.get_wav_data())
#
#                 # Write wav data to the temporary file as bytes.
#                 with open(temp_file, 'w+b') as f:
#                     f.write(wav_data.read())
#
#                 with torch.no_grad():
#                     # Read the transcription.
#                     result = audio_model.transcribe(temp_file, fp16=torch.cuda.is_available())
#                     text = result['text'].strip()
#
#                 # If we detected a pause between recordings, add a new item to our transcripion.
#                 # Otherwise edit the existing one.
#                 if phrase_complete:
#                     transcription.append(text)
#                 else:
#                     transcription[-1] = text
#
#                 # Clear the console to reprint the updated transcription.
#                 os.system('cls' if os.name == 'nt' else 'clear')
#
#                 #################################################################################################
#                 for line in transcription:
#
#                     runner = 0
#                     popped = False
#                     while runner < len(phrases):
#                         x = phrases[runner]
#                         # x is a dict with time as a datetime.now() object, and message
#                         if x['time'] == datetime.now():
#                             phrases.pop(runner)
#                             runner -= 1
#                         if x['text'] == line:
#                             popped = True
#                         runner += 1
#                     if not popped:
#                         phrases.append({'time': (datetime.now() + timedelta(minutes=1)), 'text': line})
#                     if line == 'Thank You.' or line == 'Thanks for watching!':
#                         # don't print if its Thank YOu. or Thanks for watching!, when it doesn't know if
#                         # anything is being said it will likely print out either of these
#                         break
#                     else:
#                         print(f"BUGGY  ln: {line}")
#                     if 'jarvis' in line or 'Jarvis' in line and len(line) > 8 and not popped:
#                         line = line.replace('jarvis', '')
#                         line = re.sub(r'[^a-zA-Z]', '', line)
#                         print(f"LINE: {line}")
#                         call_gpt(line)
#                 #######################################################################################################
#                 # Flush stdout.
#                 print('', end='', flush=True)
#
#                 # Infinite loops are bad for processors, must sleep.
#                 await asyncio.sleep(0.5)
#         except KeyboardInterrupt:
#             break
#         except Exception as e:
#             log_it(logger, e)
#
#     print("\n\nTranscription:")
#     for line in transcription:
#         print(line)
#
#
# if __name__ == "__main__":
#     pass
#     # print(datetime.now()-timedelta(hours=30))
#     # main()
#
#
# def basic_example():
#     model = whisper.load_model('small')
#     result = model.transcribe('file.mp3')
#     print('test')
#     print(result['text'])
