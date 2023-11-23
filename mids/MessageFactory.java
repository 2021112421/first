public class MessageFactory {
    public static Message getMessage(int type){
        return new Message(type);
    }
}
