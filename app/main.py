# -*- coding: utf-8 -*-
import os

from ui import BakingBreadApp


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    app = BakingBreadApp("breadDataset.csv")
    app.mainloop()


if __name__ == "__main__":
    main()
