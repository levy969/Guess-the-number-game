import random
def main():
    random.seed()
    while True:
        moni=False
        onetime=True
        chances=5
        randomm=random.randint(1,100)
        previous_guess=set()
        s=input("enter any key if you want to start game or press q to quit : ")
        if s.lower() == 'q':
            break
        else:
            print('you have 5 chances and if you guess closer in first 3 try u will be rewarded with 1 extra chance')
            while chances > 0 :
                print(f"remaining chances :{chances}")
                try:
                    guess=int(input('enter a guess'))
                except ValueError:
                    continue

                if guess==randomm:
                    moni=True
                    break
                if guess in previous_guess:
                    print('you alr guessed try diff')
                    continue
                previous_guess.add(guess)
                if abs(guess - randomm) <= 10 and chances>2 and onetime:
                    print('congrats you hit the jack')
                    chances+=1
                    onetime=False
                else:
                    print('guess again')
                chances-=1

            if moni:
                print('congrats you just won')
            else:
                print('better luck next time')
                print(f'secret number was : {randomm}')


if __name__ == "__main__" :
    main()
