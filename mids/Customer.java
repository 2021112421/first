public class Customer {
    private String name;
    private Queue queue;

    public Customer(MessageQueue messageQueue,String name){
        this.name = name;
        queue = new Queue(name);
        messageQueue.addQueue(queue);
    }

    public String getName(){
        return name;
    }
    public String receive(){
        return queue.output().getData();
    }

    public static void main(String[] args) {

        /**
         * 消息类型：
         * 1：全广播式
         * 2：选择广播式-发布订阅
         * 3：选择广播式-点对点
         */
        MessageQueue messageQueue = new MessageQueue();

        Customer customer1 = new Customer(messageQueue,"1");
        Customer customer2 = new Customer(messageQueue,"2");

        messageQueue.addSubstitute(customer2);

        Product product = new Product(messageQueue);

        product.send(1,"i love you all");
        product.send(2,"i love you who love me");
        product.send(3,"i only love you",customer1);

        System.out.println(customer1.receive());
        System.out.println(customer1.receive());
        System.out.println(customer2.receive());
        System.out.println(customer2.receive());
    }
}
