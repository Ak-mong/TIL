public class Main {
    public static void main(String[] args) {
        int N = 6;
        int[] resultArray= new int[5];
        for (int i=0; i < resultArray.length; i++){
            resultArray[i] = (int) (Math.random() + N) +1;
            
        }

        System.out.println("Hello world!");
    }
}