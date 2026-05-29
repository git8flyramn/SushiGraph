import matplotlib.pyplot as plt
import matplotlib_fontja


plt.rcParams["font.family"] = "IPAexGothic"


def plot_data():
    plt.title("回転寿司チェーン店の15貫あたりの重さと値段")
    plt.xlabel("重さ(g)")
    plt.ylabel("値段(円)")
        # 15貫の重さ　値段 15貫
    
    plt.plot(438.7,968,marker=".",color="#0066FF",label="はま寿司",ms = 32)
    print("はま寿司",438.7/968) #1円当たり何グラム
    plt.plot(421.3,1730,marker=".",color="#00CC00",label="平禄寿司",ms = 32)
    print("平禄寿司",421.3/1730)
    plt.plot(344.7,920,marker=".",color="#000000",label="くら寿司",ms = 32)
    print("くら寿司",344.7/920)
    plt.plot(407.0,1200,marker=".",color="#FF0000",label="スシロー",ms = 32)
    print("スシロー",407.0/1200)
    plt.plot(345.0,1120,marker=".",color="#FFD700",label="魚べい",ms = 32)
    print("魚べい",345.0/1120)
    plt.legend()
    plt.show()

   




plot_data()



