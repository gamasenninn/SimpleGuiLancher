import subprocess
import threading

def read_output(process):
    while True:
        output = process.stdout.readline()
        if output:
            print(output.strip())
        else:
            break

# random_message.pyスクリプトを実行
process = subprocess.Popen(["python", "random_message.py"], stdout=subprocess.PIPE, text=True)

# 別スレッドで出力を読み取る
thread = threading.Thread(target=read_output, args=(process,))
thread.start()

try:
    # メインスレッドではプロセスが終了するのを待つ
    process.wait()
except KeyboardInterrupt:
    process.kill()
    thread.join()
