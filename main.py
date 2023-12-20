from blackjack import play
from factorial import factorial
from sort_array import sort_array
from sort_numbers import sort_numbers


def main():
    # Girilen sayının faktöriyelini hesaplayan fonksiyon
    number: int = factorial(5)
    print(number)
    # Girilen iki sayıyı büyükten küçüğe sıralayan fonksiyon
    sorted_numbers: (int, int) = sort_numbers(10, 20)
    print(sorted_numbers)
    # Girilen sayı listesindeki elemanları büyükten küçüğe sıralayan fonksiyon (Bubble Sort)
    array = [88, 113, 717, 86, 58, 788, 527, 535, 83, 283, 976, 686, 803, 879, 380]
    print(sort_array(array))
    # Blackjack
    print("---------Blackjack---------")
    play()


if __name__ == "__main__":
    main()
