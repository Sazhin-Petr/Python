s = " I am leaning Python. hello, WORLD!"
st = s[s.find("h") + 1:s.rfind("h")]
rev_st = st[::-1]
print(s[:s.find("h") + 1] + rev_st + s[s.rfind("h"):])

