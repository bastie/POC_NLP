/**
 * 
 */
package biz.ritter.nltk.book.preface;

import java.nio.file.Files;
import java.nio.file.Paths;

/**
 * very simple Java version
 * @author Sͬeͥbͭaͭsͤtͬian
 * @version 0.1
 */
public final class WhyJava {
  
  public static void main(final String... args) throws Throwable {
    for (String line : Files.readAllLines(Paths.get("file.txt"))) {
      for (String word : line.split (" ")) {
        if (word.endsWith("ing")) {
          System.out.printf("%s%n", word);
        }
      }
    }
  }
  
}
