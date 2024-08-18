class Animal {
    public void makeSound() {
        System.out.println("동물 소리");
    }
}

class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("멍멍");
    }
}

class Cat extends Animal {
    @Override
    public void makeSound() {
        System.out.println("야옹");
    }
}
class PolyTest{
    public static void main(String[] args){
        Customer c = new Customer("은행나무","대구",24);
        System.out.println(c);

        MainCustomer mc = new MainCustomer("소나무", "부산", 21, "여행");
        System.out.println(mc);

        Customer cc  = new MainCustomer("강나루", "인천", 25, "게임");
                System.out.println(cc);
    }
}
public class Main {
    public static void main(String[] args) {
        Animal animal1 = new Dog();
        Animal animal2 = new Cat();

        animal1.makeSound(); // 출력: 멍멍
        animal2.makeSound(); // 출력: 야옹
    }
}