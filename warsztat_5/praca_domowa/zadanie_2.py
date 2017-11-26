# Napisz funkcję longest_collatz(start, stop)
# Funkcja ma zwracać długość najdłuższej sekwencji Collatza i wartość startową dla wartości od ‘start’ włącznie, do ‘stop’ wyłącznie.
# W tym zadaniu można (lecz nie ma przymusu) użyć generatorów.
# Proszę o wykorzystanie kodu z zadania 1 (przeklejcie kod do tego zadania, żeby uniknąć problemów z importami, to nie zadanie na sprawdzenie importowania)


# class CollatzSeq:
#     def __init__(self, start_value):
#         self.sv = start_value
#
#         if type(start_value) is not int:
#             raise ValueError
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.sv == 0.5:
#             raise StopIteration
#         elif self.sv %2 == 0:
#             self.sv = self.sv/2
#             return self.sv*2
#         elif self.sv%2 != 0 and self.sv!=1:
#             self.sv = 3*self.sv + 1
#             return (self.sv-1)/3
#         elif self.sv == 1:
#             self.sv = 0.5
#             return 1

class CollatzSeq:
    def __init__(self, start_value):
        self.sv = start_value

        if type(start_value) is not int:
            raise ValueError

    def __iter__(self):
        return self

    def __next__(self):
        if self.sv == 0.5:
            raise StopIteration
        elif self.sv %2 == 0:
            self.sv = self.sv/2
            return self.sv*2
        elif self.sv%2 != 0 and self.sv!=1:
            self.sv = 3*self.sv + 1
            return (self.sv-1)/3
        elif self.sv == 1:
            self.sv = 0.5
            return 1

def longest_collatz(start, stop):
    d = {}
    longest_seq = 0
    for i in range(start, stop+1):
        seq_counter = 0
        for c in CollatzSeq(i):
            seq_counter +=1
        d[i] = seq_counter
        if seq_counter > longest_seq:
            longest_seq = seq_counter

    for k, v in d.items():
        if v == longest_seq:
            return (v, k)


#
# counter=0
# for c in CollatzSeq(5):
#     counter+=1
#     print(int(c))
# print(70*'-')
# print(counter)
# print(70*'-')
# counter=0
# for c in CollatzSeq(6):
#     counter+=1
#     print(int(c))
# print(70*'-')
# print(counter)
# print(70*'-')
# counter=0
# for c in CollatzSeq(7):
#     counter+=1
#     print(int(c))
# print(70*'-')
# print(counter)
# print(70*'-')
# counter=0
# for c in CollatzSeq(8):
#     counter+=1
#     print(int(c))
# print(70*'-')
# print(counter)
# print(70*'-')
# counter=0
# for c in CollatzSeq(9):
#     counter+=1
#     print(int(c))
# print(70*'-')
# print(counter)

print(longest_collatz(1, 10**6))
#
if __name__ == '__main__':
    # assert longest_collatz(1, 2) == (1, 1)
    # assert longest_collatz(2, 3) == (2, 2)
    assert longest_collatz(3, 4) == (len([3, 10, 5, 16, 8, 4, 2, 1]), 3)
    assert longest_collatz(12, 13) == (len([12, 6, 3, 10, 5, 16, 8, 4, 2, 1]), 12)
    assert longest_collatz(19, 20) == (len([19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]), 19)
    assert longest_collatz(27, 28) == (len([27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]), 27)
    assert longest_collatz(12346789, 12346790) == (len([12346789, 37040368, 18520184, 9260092, 4630046, 2315023, 6945070, 3472535, 10417606, 5208803, 15626410, 7813205, 23439616, 11719808, 5859904, 2929952, 1464976, 732488, 366244, 183122, 91561, 274684, 137342, 68671, 206014, 103007, 309022, 154511, 463534, 231767, 695302, 347651, 1042954, 521477, 1564432, 782216, 391108, 195554, 97777, 293332, 146666, 73333, 220000, 110000, 55000, 27500, 13750, 6875, 20626, 10313, 30940, 15470, 7735, 23206, 11603, 34810, 17405, 52216, 26108, 13054, 6527, 19582, 9791, 29374, 14687, 44062, 22031, 66094, 33047, 99142, 49571, 148714, 74357, 223072, 111536, 55768, 27884, 13942, 6971, 20914, 10457, 31372, 15686, 7843, 23530, 11765, 35296, 17648, 8824, 4412, 2206, 1103, 3310, 1655, 4966, 2483, 7450, 3725, 11176, 5588, 2794, 1397, 4192, 2096, 1048, 524, 262, 131, 394, 197, 592, 296, 148, 74, 37, 112, 56, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]), 12346789)
    assert longest_collatz(1, 10**6) == (525, 837799)
