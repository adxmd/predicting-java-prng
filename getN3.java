import java.util.Random;
import java.util.Scanner;

public class getN3 {
    public static void main(String[] args) {
    Scanner scanObj = new Scanner(System.in);
    System.out.println("Enter secret seed outputted from bruteForce.py: ");
    String seed = scanObj.nextLine();
    long secret_seed = Long.parseLong(seed);

    // long secret_seed = 232595392581409L;

    Random rand = new Random( secret_seed );
    int n1 = rand.nextInt();
    int n2 = rand.nextInt();  
    System.out.println("n2: ");
    System.out.println(n1);
    System.out.println("n3: ");
    System.out.println(n2);
    // System.out.println(n3);
    scanObj.close();
}
}
