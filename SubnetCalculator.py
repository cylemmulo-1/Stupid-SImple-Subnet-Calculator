subnum = input("Enter a CIDR subnet mask 25-31:")

if subnum == "25" or subnum == "/25":
    newnum25 = int(input("Either 0 128:"))
    print (f".{newnum25} - {newnum25 + 127}")
elif subnum == "26" or subnum == "/26":
    newnum26 = int(input("Either 0 64 128 192:"))
    print (f".{newnum26} - {newnum26 + 63}")
elif subnum == "27" or subnum == "/27":
    newnum27 = int(input("Either 0 32 64 96 128 160 192 224:"))
    print (f".{newnum27} - {newnum27 + 31}")
elif subnum == "28" or subnum == "/28":
    newnum28 = int(input("Either 0 16 32 48 64 80 96 112 128 144 160 176 192 208 224 240:"))
    print (f".{newnum28} - {newnum28 + 15}")
elif subnum == "29" or subnum == "/29" :
    newnum29 = int(input("Either 0 8 16 24 32 40 48 56 64 72 80 88 96 104 112 120 128 136 144 152 160 168 176 184 192 200 208 216 224 232 240 248:"))
    print (f".{newnum29} - {newnum29 + 7}")
elif subnum == "30" or subnum == "/30" :
    newnum30 = int(input("Either 0 4 8 12 16 20 24 28 32 36 40 44 48 52 56 60 64 68 72 76 80 84 88 92 96 100 104 108 112 116 120 124 128 132 136 140 144 148 152 156 160 164 168 172 176 180 184 188 192 196 200 204 208 212 216 220 224 228 232 236 240 244 248 252:"))
    print (f".{newnum30} - {newnum30 + 3}")
elif subnum == "31" or subnum == "/31":
    newnum31 = int(input("Either 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100 102 104 106 108 110 112 114 116 118 120 122 124 126 128 130 132 134 136 138 140 142 144 146 148 150 152 154 156 158 160 162 164 166 168 170 172 174 176 178 180 182 184 186 188 190 192 194 196 198 200 202 204 206 208 210 212 214 216 218 220 222 224 226 228 230 232 234 236 238 240 242 244 246 248 250 252 254:"))
    print (f".{newnum31} - {newnum31 + 1}")
else :
    print("25-31 only")
k=input("press any key to exit")
