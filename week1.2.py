# Downloads Qantas share price beginning 1 January 2020
import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')                              # (7)

a="1"+"2"
print(a)

b=2/1
print(b)
print(type(b))

a1=1
print(a1)

toolkit/
|__ venv/                             <- folder containing system files
|   |__ <bunch of files/folders>
|__ main.py
|__ yf_example1.py

a=3
a=a+3
print(a)

a2=6
a2=a2+8
print (a2)

x=1
xstr=1
test=x==xstr

print(3+2)
print("3"+"2")