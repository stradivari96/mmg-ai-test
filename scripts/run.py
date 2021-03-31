import sys, os

sys.path.append(os.getcwd())

from mmg_ai_test.app import app


if __name__ == "__main__":
    app.run()
