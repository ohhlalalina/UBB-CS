package root;

import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class MyBlockingQueue<Element> {
    private Queue<Element> queue;
    private int max = 20;
    private ReentrantLock lock = new ReentrantLock(true);
    private Condition var;

    public MyBlockingQueue(int size, ReentrantLock lock){
        queue = new LinkedList<>();
        this.max = size;
        this.lock = lock;
        this.var = lock.newCondition();
    }

    public void put(Element e){
        lock.lock();
        try{
            if(queue.size() == max){
                var.await();
            }
            queue.add(e);
            var.signalAll();
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        } finally {
            lock.unlock();
        }
    }

    public Element take(){
        lock.lock();
        try{
            if(queue.size() == 0){
                var.await();
            }
            Element item = queue.remove();
            var.signalAll();
            return item;
        } catch (InterruptedException e) {
            e.printStackTrace();
            return null;
        } finally{
            lock.unlock();
        }
    }
}
