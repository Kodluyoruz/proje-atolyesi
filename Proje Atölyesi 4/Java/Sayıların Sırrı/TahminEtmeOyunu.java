package kodluyoruzodev;
import java.util.Scanner;
import java.util.Random;
public class TahminEtmeOyunu {

	public static void main(String[] args) {
		

		 

		     
		        Scanner scanner = new Scanner(System.in);
		        Random random = new Random();
		        
		        int maksimumSayi = 100; // Rastgele seçilecek sayının maksimum değeri
		        int gizliSayi = random.nextInt(maksimumSayi) + 1; // 1 ile maksimumSayi arasında rastgele bir sayı seçiliyor
		        int tahmin;
		        int tahminSayisi = 0;
		        
		        System.out.println("Tahmin Etme Oyunu'na hoş geldiniz!");
		        System.out.println("1 ile " + maksimumSayi + " arasında bir sayıyı tahmin etmeye çalışın.");

		        do {
		            System.out.print("Tahmininiz: ");
		            tahmin = scanner.nextInt();
		            tahminSayisi++;
		            
		            if (tahmin < gizliSayi) {
		                System.out.println("Daha büyük bir sayı girin.");
		            } else if (tahmin > gizliSayi) {
		                System.out.println("Daha küçük bir sayı girin.");
		            } else {
		                System.out.println("Tebrikler, doğru tahmin! Gizli sayı: " + gizliSayi);
		                System.out.println("Tahmin sayınız: " + tahminSayisi);
		                break;
		            }
		        } while (true);
		        
		        scanner.close();
		    }
		

	}


