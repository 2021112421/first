public class Product {
    MessageQueue messageQueue;

    public Product(MessageQueue messageQueue){
        this.messageQueue = messageQueue;
    }

    public void send(int type,String data){
        messageQueue.input(new Message(type,data));
    }

    public void send(int type,String data,Customer target){
        messageQueue.input(new Message(type,data,target.getName()));
    }
}
