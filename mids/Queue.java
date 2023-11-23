import java.util.concurrent.LinkedBlockingQueue;

public class Queue {
    private LinkedBlockingQueue<Message> messages = new LinkedBlockingQueue<>();
    private String target;

    public Queue(String target) {
        this.target = target;
    }

    public String getTarget() {
        return target;
    }

    public Message output(){
        try {
            return messages.take();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return new Message(0);
    }

    public boolean input(Message message){
        try {
            messages.put(message);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return true;
    }


}
