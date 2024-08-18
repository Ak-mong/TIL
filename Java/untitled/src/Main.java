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

public class Main {
    public static void main(String[] args) {
        Animal animal1 = new Dog();
        Animal animal2 = new Cat();

        animal1.makeSound(); // 출력: 멍멍
        animal2.makeSound(); // 출력: 야옹
    }
}