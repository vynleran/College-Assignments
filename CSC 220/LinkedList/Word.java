public class Word {

    String word;
    int wordCount;

    public Word(String w){
        this.word = w;
        this.wordCount = 1;
    }

    /*Getter and setter for word*/
    public void setWord(String w) {
        this.word = w;
    }
    public String getWord() {
        return this.word;
    }

    /*Getter and setter for wordCount*/
    public void setWordCount(int wc) {
        this.wordCount = wc;
    }
    public int getWordCount() {
        return this.wordCount;
    }

    // Adding one to the word count
	public void incCount() {
        wordCount++;
	}
}
