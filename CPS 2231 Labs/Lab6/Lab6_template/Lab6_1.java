public class Lab6_1 {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java Lab6_1 <test_type>");
            return;
        }

        String testType = args[0];
        switch (testType) {
            case "Bird":
                Bird bird = new Bird();
                bird.move();
                bird.makeSound();
                break;
            case "Panthera":
                Panthera panthera = new Panthera();
                panthera.move();
                panthera.makeSound();
                break;
            case "Animal":
                Animal animal = new Animal();
                animal.move();
                animal.makeSound();
                break;
            case "PolyBird":
                Animal polyBird = new Bird();
                polyBird.move();
                polyBird.makeSound();
                break;
            case "PolyPanthera":
                Animal polyPanthera = new Panthera();
                polyPanthera.move();
                polyPanthera.makeSound();
                break;
        }
    }
}

// TODO: Create the Animal class here
// The Animal class should have two methods:
// 1. move() - prints "Animal moves"
// 2. makeSound() - prints "Animal makes a sound"
class Animal {
    // Your code here
}

// TODO: Create the Bird class here
// The Bird class should inherit from Animal and override both methods:
// 1. move() - prints "Bird flies through the air"
// 2. makeSound() - prints "Bird chirps"
class Bird {
    // Your code here
}

// TODO: Create the Panthera class here
// The Panthera class should inherit from Animal and override both methods:
// 1. move() - prints "Panthera stalks through the grass"
// 2. makeSound() - prints "Panthera roars"
class Panthera {
    // Your code here
} 