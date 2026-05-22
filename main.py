import matplotlib.pyplot as plt
import matplotlib_fontja

plt.rcParams["font.family"] = "IPAexGothic"
def plot_data():
    plt.title("寿司屋の重さと値段グラフ")
    plt.xlabel("重さ(g)")
    plt.ylabel("値段(円)")
    plt.plot(10,150,marker=".",color="blue",label="はま寿司")
    plt.legend()
    plt.show()

plot_data()


