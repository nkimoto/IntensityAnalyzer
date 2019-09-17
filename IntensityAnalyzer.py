# coding: utf-8

import os
import tkinter as tk
from tkinter import ttk, StringVar, LEFT, filedialog
import matplotlib.pyplot as plt
import pandas as pd


class IntensityAnalyzer(tk.Frame):
    """
    Args:
        root: 親となるTkインスタンス
    """
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        root.title('Pack Three Labels')
        root.resizable(False, False)
        self.widget()

    def widget(self):
        """
        ウィジェットの作成
        """
        # Frame1の作成
        self.frame1 = ttk.Frame(self.root, padding=10)
        self.frame1.grid()

        # 参照ボタンの作成
        self.button1 = ttk.Button(self.root, text=u'参照',
                                  command=self.button1_clicked)
        self.button1.grid(row=0, column=3)

        # ラベルの作成
        # 「ファイル」ラベルの作成
        self.s = StringVar()
        self.s.set('ファイル>>')
        self.label1 = ttk.Label(self.frame1, textvariable=self.s)
        self.label1.grid(row=0, column=0)

        # 参照ファイルパス表示ラベルの作成
        self.file1 = StringVar()
        file1_entry = ttk.Entry(self.frame1, textvariable=self.file1, width=50)
        file1_entry.grid(row=0, column=2)

        # Frame2の作成
        self.frame2 = ttk.Frame(self.root, padding=(0, 5))
        self.frame2.grid(row=1)

        # Startボタンの作成
        self.button2 = ttk.Button(self.frame2, text='グラフ表示',
                                  command=lambda:
                                  self.button2_clicked(self.file1.get()))
        self.button2.pack(side=LEFT)

        # Cancelボタンの作成
        self.button3 = ttk.Button(self.frame2, text='Cancel', command=quit)
        self.button3.pack(side=LEFT)

    def button1_clicked(self):
        """
        参照ボタンのイベント
        button1クリック時の処理
        """
        fTyp = [("csv files", "*.csv")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        filepath = filedialog.askopenfilename(filetypes=fTyp,
                                              initialdir=iDir)
        self.file1.set(filepath)

    def button2_clicked(self, target_file):
        """
        Args:
            target_file: プロットに使用するCSVファイル

        button2クリック時の処理
        """
        df = pd.read_csv(target_file, index_col=0)
        df = df.iloc[:, [4, 5, 6, 7, 8, 9, 11]]
        df.columns = [u'a', u'b', u'c', u'd', u'e', u'f', u'g']
        df.plot(subplots=True, figsize=(10, 6))
        plt.show()


def main():
    win = tk.Tk()
    app = IntensityAnalyzer(root=win)
    app.mainloop()


if __name__ == "__main__":
    main()
