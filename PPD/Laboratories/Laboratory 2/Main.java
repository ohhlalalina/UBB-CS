package root;

import java.util.Random;
import java.util.concurrent.locks.ReentrantLock;

public class Main {

    public static void main(String[] args) throws InterruptedException {
	    int size = 100;
	    Random r = new Random();
	    int[] vector1 = new int[size];
	    int[] vector2 = new int[size];
	    for(int i=0; i<size; i++){
	        vector1[i] = r.nextInt() % 50;
	        vector2[i] = r.nextInt() % 50;
        }
        int s = 0;
        for(int i=0; i<size; i++)
            s += vector1[i]*vector2[i];
        System.out.println("seq. result: "+s);
        ReentrantLock lock = new ReentrantLock();
        MyBlockingQueue<Integer> blockingQueue =  new MyBlockingQueue<>(r.nextInt() % 20, lock);

        Runnable consumer = () ->{
            Integer sum=0;
            for(int i=0;i<size;i++){
            Integer received = blockingQueue.take();
            if(received != null){
                sum += received;}}
            System.out.println("The scalar product is "+sum);
        };

        Runnable producer = () ->{
            for(int i=0;i<size; i++){
                blockingQueue.put(vector1[i]*vector2[i]);
            }
        };

        Thread cons = new Thread(consumer);
        Thread prod = new Thread(producer);
        cons.start();
        prod.start();
        cons.join();
        prod.join();
    }
}
