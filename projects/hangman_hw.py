class Hangman:
    def __init__(self, secret_word):
        self.secret_word = secret_word.lower()
        self.guessed_letters = []
        self.max_mistakes = 6
        self.mistakes = 0

    def display_word(self):
        shown_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                shown_word += letter + " "
            else:
                shown_word += "_ "
        return shown_word

    def guess_letter(self, letter):
        letter = letter.lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Моля, въведи само една буква!")
            return

        if letter in self.guessed_letters:
            print("Вече си пробвал тази буква!")
            return

        self.guessed_letters.append(letter)

        if letter in self.secret_word:
            print("Позна! :)")
        else:
            print("Грешка! :( ")
            self.mistakes += 1
            print("Грешки:", self.mistakes, "/", self.max_mistakes)

    def is_won(self):
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False
        return True

    def is_lost(self):
        return self.mistakes >= self.max_mistakes



game = Hangman("котка")

print("Добре дошъл в играта 'Бесеница'!")
print("Опитай се да познаеш думата буква по буква.\n")

while True:
    print("Дума:", game.display_word())

    if game.is_won():
        print("Браво! Позна думата:", game.secret_word)
        break

    if game.is_lost():
        print("Загуби! Думата беше:", game.secret_word)
        break

    guess = input("Въведи буква: ")
    game.guess_letter(guess)

print("Край на играта!")



# при обектно ориентираното програмиране искаш цялата логика свързана с класа да бъде вътре в него
# цикълът в който се въртят ходовете на играта трябва да влезе в метод play_game в класа (play_game е само примерно име)
# накрая искаш като създадеш обект да му извикаш метода play_game
while True:
    print("Дума:", game.display_word())

    if game.is_won():
        print("Браво! Позна думата:", game.secret_word)
        break

    if game.is_lost():
        print("Загуби! Думата беше:", game.secret_word)
        break

    # с така дефинирана логиката, този безкраен цикъл репрезентира един ход в играта. Би било по-добре вместо
    # на един ход да правиш един опит и да преминаваш към следващия ход, да взимаш Input докато ходът не стане валиден
    # и тогава да извършваш останалите действия и да преминаваш към следващ ход. Тази разлика ще стане по-ясна в
    # контекста на морския шах и други по-сложни програми
    guess = input("Въведи буква: ")
    game.guess_letter(guess)

print("Край на играта!")

# Виждам, че си разбрал основните концепции на ООП, приложил си правилно дефинирането на клас, инстанциирането на обект
# и извикването на метод на обект. Би могъл да добавиш енкапсулация чрез _ и __ в началото на имената на променливи и
# методи които не се достъпват извън дефиницията. Добра работа!
