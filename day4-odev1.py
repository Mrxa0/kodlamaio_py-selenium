#HTML 

#HTML açılımı “Hyper Text Markup Language” olarak bilinir.HTML bir web sitesinin iskeletidir.HTML web tarayıcıların web sitelerimizi tanımasına yarayan bir dildir.

#***SIK KULLANILAN HTML TAG'LERİ***

#<html> </html> baş etikettir bütün kodlar bu etiketin arasında olmalıdır.

#<body> </body> Ekrana yansıyacak bütün kodlar body'nin arasında yer alır.

#<head> </head> Web sayfasının dili başlığı ve diğer düzenlemelerinin yer aldığı etikettir.

#HTML link verme kodlarından biri olan <a> kodu ile diğer içerikleriniz arasında da bağlantılar oluşturabilirsiniz.

#<div> </div> sayfayı içerisini içeriklerle doldurabileceğimiz kutulara böler.


#FORMLAR

#Bu etiket sayesinde, metin alanları, onay kutuları, radyo butonları, gönderme butonları vb. gibi girdi elemanlarını kullanırız.
#<form>

#<p>İSİM</p>
#<input type="text">
#<input type="button" value="Gönder"> BUTON EKLER

#</form>

#ID ve CLASS 

#ID tek bir elemente verilir başka bir elementte kullanılmaması gerekir.

#Class ortak özelliklere sahip olan elementler için kullanılır.


#***HTML Locators***

#Locators,Selenium IDE’ye hangi web tabanlı objeler üzerinde çalışması gerektiğini söyleyen bir komuttur.Site üzerindeki bir elemente örneğin giriş butonuna selenium ile tıklama işlemi yaptırmak istediğimizde bu işlemi locator’lar aracılığıyla yaparız. Selenium ile geliştirmek istediğimiz test otomasyonlarında locator’ları kullanarak ilgili alanlara veri gönderebilir, tıklama işlemi yaptırabilir, var olan içeriği temizleyebiliriz.Bunlar ‘By’ objesi olarak oluşturulur.
#En yaygın locator çeşitleri;
#ID
#Name
#ClassName
#TagName
#LinkText
#CssSelector
#XPath

#Web sitelerdeki tagname'lerin sahip olduğu name,stil,id nitelikleri vardır.Bu nitelikleri selenium'un anlayacağı şekile çevirirken ilk id'si ve name'i ne bakılır ya da CssSelector ve Xpath ile nesneyi buluruz.

# SELENIUM'DA AKSİYONLAR

#driver.get() - Gitmek istenilen web sitesinin url'si çağırılır.
#
#driver.title - Girilen web sitesinin başlık etiketi içerisindeki metne ulaşmak için kullanılır.
#
#driver.back() - Site içerisinde farklı sayfalara girmiş isek geri gitmek için back kullanılır.
#
#driver.refresh() - Sayfayı yeniler.
#
#driver.close() - Sadece açılan sekmeyi kapatır.
#
#driver.quit() - Tarayıcıyı kapatır.
#
#driver.maximize_window() - Açılan sayfayı tam ekran yapar.
#
#driver.set_window_size(800,600) - Açılan sayfanın boyutlarını kendimiz de seçebiliriz.
#
#driver.save_screenshot("dosya yolu") True - Açılan sayfanın ekran görüntüsünü kayıt eder.Ve bu method başarılı bir şekilde çalışırsa True değeri geri döner
#
#driver.page_source - sayfa kaynak koduna ulaşmamızı sağlar.
#
#
#
#
