# 1
tub_sonlar = {
    n for n in range(2, 51)
    if all(n % d != 0 for d in range(2, int(n**0.5) + 1))
}
print(tub_sonlar)

# 2
sozlar = ["apple", "banana", "orange", "ice", "umbrella", "code"]

unlilar = "aeiouAEIOU"

unli_bosh_set = {s for s in sozlar if s[0] in unlilar}
print(unli_bosh_set)

# 3
matn = "Hello World"

unikal_harflar = {ch for ch in matn}
print(unikal_harflar)

# 4
toq_kublar = {n**3 for n in range(1, 31) if n % 2 == 1}
print(toq_kublar)

# 5
soz = "Python"

ascii_set = {ord(ch) for ch in soz}
print(ascii_set)

# 6
words = ["python", "java", "c", "html", "css", "node"]

uzunliklar = {len(s) for s in words}
print(uzunliklar)

# 7
holat_set = {
    f"{n}-even" if n % 2 == 0 else f"{n}-odd"
    for n in range(1, 21)
}
print(holat_set)

# 8
sozlar = ["python", "set", "loop", "data"]

oxirgi_harflar = {s[-1] for s in sozlar}
print(oxirgi_harflar)

# 9
matnlar = ["hello123", "world", "python3", "code", "a1b"]

raqam_borlar = {s for s in matnlar if any(ch.isdigit() for ch in s)}
print(raqam_borlar)

# 10
Misol:

23 → 2×3 = 6

61 → 6×1 = 6

kopaytma_6 = {
    n for n in range(1, 51)
    if (lambda x: eval("*".join(x)))([d for d in str(n)])
    == 6
}
