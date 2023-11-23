public class Message {
    private int type;
    private String data;
    private String target;

    public Message(int type) {
        this.type = type;
        this.target = "";
    }

    public Message(int type,String data) {
        this.type = type;
        this.target = "";
        this.data = data;
    }

    public Message(int type,String data,String target) {
        this.type = type;
        this.target = target;
        this.data = data;
    }

    public  int getType(){
        return this.type;
    }

    public String getData() {
        return data;
    }

    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }

    public void setType(int type) {
        this.type = type;
    }

    public void setData(String data) {
        this.data = data;
    }
}
