public class Book {
	private String title;
	private String author;
	private boolean status;
	private int priority;
	
	public Book()
	{
		title = "";
		author = "";
	}
	public Book(String t, String a, boolean s, int p)
	{
		title = t;
		author = a;
		status = s;
		priority = p;
		
	}

	public String getTitle()
	{
		return title;
	}
	public void setTitle(String t)
	{
		title  = t;
	}
	public String getAuthor()
	{
		return author;
	}
	public void setAuthor(String a)
	{
		author = a;
	}
	public boolean getStatus()
	{
		return status;
	}
	public void setStatus()
	{
		status = !status;
	}
	public int getPriority()
	{
		return priority;
	}
	public void setPriorirty(int p)
	{
		priority = p;
	}
	public String toString(){
		// if(status = true){
		// 	return("Author: " + author + "\t\tStatus: Row " + priority);
		// }
		// else {
		// 	return("Author: " + author + "\t\tStatus: Taken");
		// }
		return("Title: " + title + "\t\tAuthor: " + author + "\t\tStatus: " + status);
	}
}
