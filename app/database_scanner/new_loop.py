import os


def run_script():
    script_file = 'create_alarm.ps1'
    os.system(f'powershell -File "{script_file}"')

if __name__ == '__main__':
    run_script()