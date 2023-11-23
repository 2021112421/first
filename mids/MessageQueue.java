import javax.jws.Oneway;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class MessageQueue {
    private List<Queue> queues = new LinkedList<>();
    private List<String> substitutes = new ArrayList<>();
    public MessageQueue(){

    }
    public void addQueue(Queue queue){
        queues.add(queue);
    }
    public void addSubstitute(String target){
        substitutes.add(target);
    }
    public void addSubstitute(Customer customer){
        substitutes.add(customer.getName());
    }

    public void input(Message message){
        if (message.getType()==1){
            for (Queue q :queues){
                q.input(message);
            }
        }
        else if (message.getType()==2){
            for (Queue q:queues){
                for (String s:substitutes){
                    if (s.equals(q.getTarget())){
                        q.input(message);
                    }

                }

            }
        }
        else if (message.getType()==3){
            for (Queue q:queues){
                if (q.getTarget().equals(message.getTarget()))
                    q.input(message);
            }
        }

    }
}
