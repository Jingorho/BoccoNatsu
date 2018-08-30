# coding: utf-8
# 2018.08.29

def setTheme(theme):
	with open('data/theme.txt', mode='w') as f:
		f.write(str(theme))

if __name__ == "__main__":
    setTheme()