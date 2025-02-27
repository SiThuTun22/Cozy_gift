document.querySelector(".read-more").addEventListener("click", function () {
    const texts = document.querySelectorAll(".text-hidden-my"); // All hidden paragraphs
    const firstText = document.querySelector(".content-paragraph-my.visible"); // First visible paragraph
    const isAllVisible = Array.from(texts).every(text => text.classList.contains("visible")); // Check visibility
  
    if (isAllVisible) {
      // Hide all paragraphs except the first
      texts.forEach(text => text.classList.remove("visible"));
      firstText.classList.add("visible"); // Ensure first paragraph stays visible
      this.textContent = "READ MORE ↓";
    } else {
      // Show all paragraphs
      texts.forEach(text => text.classList.add("visible"));
      this.textContent = "READ LESS ↑";
    }
  });
  
document.addEventListener("DOMContentLoaded", function () {
  const langEl = document.querySelector('.langWrap');
  const links = langEl.querySelectorAll('a');
  const title1 = document.querySelector('.title1');
  const title2 = document.querySelector('.title2');
  const title3 = document.querySelector('.title3');
  const title4 = document.querySelector('.title4');
  const title5 = document.querySelector('.title5');
  const title6 = document.querySelector('.title6');
  const descrEl1 = document.querySelector('.description1');
  const descrEl2 = document.querySelector('.description2');
  const descrEl3 = document.querySelector('.description3');
  const descrEl4 = document.querySelector('.description4');
  const descrEl5 = document.querySelector('.description5');
  const descrEl6 = document.querySelector('.description6');
  const descrEl7 = document.querySelector('.description7');

  links.forEach(el => {
    el.addEventListener('click', (e) => {
      e.preventDefault();

      langEl.querySelector('.active').classList.remove('active');
      el.classList.add('active');

      const attr = el.getAttribute('language');

      title1.textContent = data[attr].title1;
      title2.textContent = data[attr].title2;
      title3.textContent = data[attr].title3;
      title4.textContent = data[attr].title4;
      title5.textContent = data[attr].title5;
      title6.textContent = data[attr].title6;
    
      descrEl1.textContent = data[attr].description1;
      descrEl2.textContent = data[attr].description2;
      descrEl3.textContent = data[attr].description3;
      descrEl4.textContent = data[attr].description4;
      descrEl5.textContent = data[attr].description5;
      descrEl6.textContent = data[attr].description6;
      descrEl7.textContent = data[attr].description7;
    });
  });

  const data = {
    "english": {
      "title1": "Flower Meanings",
      "description1": "Rose",
      "description2": "Roses, the world’s most popular flower, come in just about every color imaginable and express a vast range of emotions. Gardeners obsess over them, and even gas stations sell them. Break out the rose-colored reading glasses for a crash course in this iconic bloom.",
      "description3": " Roses, the world’s most popular flower, come in just about every color imaginable and express a vast range of emotions. Gardeners obsess over them, and even gas stations sell them. Break out the rose-colored reading glasses for a crash course in this iconic bloom.",
      "title2": "The Meanings of Roses",
      "description4": "Roses are red; violets are blue? Not quite. Roses are also white, pink, cream, peach, purple, yellow, orange, black… wait, black?There are entire books about the meanings of different roses, and what signals romance in one culture conveys sympathy in another. Consider this just a tasting course of centuries of symbolism."
      , "title3": "Rose Meanings By Color",
      "description5": "Red roses are the quintessential symbol of love. (Come on, millions of tattoos can’t be wrong.) They may be a bit of a cliché, but we’ve never met anyone who would turn down a gift of a red rose when given by someone who makes their heart go pitter-pat.White roses are for “a heart unacquainted with love,” according to Victorian lore. Whether that means the purity and innocence of youth, or the loneliness of a cold, icy heart is up to you to decide. Red and white roses in a single bouquet signify unity, a nod to the emblems of the House of Lancaster and House of York. After a generation of civil wars, the two families made peace through marriage.There aren’t many situations that pink roses don’t fit.They can express everything from gratitude to admiration to encouragement to sympathy.Mix and match to your heart’s content.The palest pink rose shows gentleness and poise.It’s also a touching way to express sympathy.Light pink roses are all about joy and happiness.Think sugar and spice, bubble gum and cotton candy, young love and first kisses.Light pink roses are drama- free love, best friend love, “love ya like a sister” love.Want to congratulate someone? You can’t go wrong with bright pink roses.They’re a welcome pick- me - up for someone who isn’t feeling well or yourself when you’re in One of Those Moods.We also love them for a “thinking of you” bouquet—like Mother’s Day for a friend whose mom has passed away.Say thank you with deep pink roses.These are a heartfelt way to express gratitude.Cream - colored roses are associated with thoughtfulness.Blushing peach roses say “modesty.” And salmon - colored roses say “desire.”[1] Cream - colored roses are associated with thoughtfulness."
      ,"title4" : "June Flower of the Month"
      , "title5": "The History of the Rose",
      "description6": "Fossils tell us that roses have existed as long as 35 million years ago, and they’ve been cultivated around the world for at least 5,000 years. Today almost all of the 1.5 billion roses that are bought in the US each year come from Colombia or Ecuador. [3]There are tea roses from China, Bourbon roses from France, and of course, there’s the American Beauty variety. It’s the official flower of the District of Columbia as well as the name of a Grateful Dead album andan Academy Award-winning movie Rose is the birth month flower of June, but its sales really peak in the US around Valentine’s Day and Mother’s Day. The Rose Parade is an American New Year’s Day tradition in Pasadena, California. Since 1890, organizations have decorated themed parade floats using hundreds of thousands of roses.If that sounds excessive, the Romans have it beat. Legend tells that the emperor Nero would rain down tons of rose petals during banquets. Cleopatra is rumored to have wooed the Roman general Mark Antony in part by filling her palace with rose petals and announcing her arrival by ship with sails soaked in fragrant rose water. As Cleopatra knew, roses are used for far more than just decoration. Rosehip tea is an excellent source of vitamin C. Rosewater is an essential ingredient in lots of Middle Eastern pastries like baklava and halva. Rose oil is a crucial ingredient in some of the world’s most lux fragrances, from brands like Dior, Balenciaga, and Prada.The unforgettable scent of roses is due to the fact that each flower might produce dozens of unique scent molecules, says ecologist Stephen Buchmann in his book, The Reason for Flowers. But rose breeders tend to focus on developing new colors or increasing bloom longevity, not creating new fragrance combinations, and so there are also completely unscented roses like the Leonidas. From the early 20th-century standard, “My Wild Irish Rose” to Bon Jovi’s ballad “Bed of Roses,” there are almost as many rose-related songs as there are varieties of the flower. For melancholy country fans, there’s George Jackson’s “A Good Year for the Roses,” and for the melancholy metalhead, there’s Poison’s “Every Rose Has Its Thorn.”",
       "title6": "How to Care for Roses",
      "description7": "There’s no big secret to keeping cut roses fresh, even for as long as two weeks. In fact, the roses you picked up might have been cut in Central America two months ago and stored in a temperature-controlled environment until shipped to the States.Once you bring your roses home, remove leaves that would be below the waterline of your vase or container. Have the vase ready with a mixture of room temperature water and a packet of floral preservative."

   


    },
  "myanmar": {
  "title1": "ပန်းအဓိပ္ပါယ်များ",
  "description1": "နှင်းဆီ",
  "description2": "နှင်းဆီသည် ကမ္ဘာ့အကျော်ကြားဆုံး ပန်းဖြစ်သည်။ ၎င်းကို သံယောဇဉ်၊ မေတ္တာနှင့် အလှပြုမှုတို့ကို ဖော်ပြရန် အသုံးပြုနိုင်သည်။",
  "description3": "နှင်းဆီသည် ကမ္ဘာ့အကျော်ကြားဆုံး ပန်းဖြစ်ပြီး မျှော်လင့်ထားသမျှ အရောင်များနှင့် တွေ့ရနိုင်ပြီး အားထားစိတ်ချမှု၊ ချစ်ခြင်းမေတ္တာနှင့် စုံလင်သောခံစားမှုများကိုဖော်ပြနိုင်သည်။ ဥယျာဉ်ထောင်သူများက နှင်းဆီများကို မဖြစ်မနေချစ်မြတ်နိုးကြပြီး သိုမှသာတောင် ဓာတ်ဆီဆိုင်များတွင်ပါ ရောင်းချနေသည်။ နှင်းဆီရောင်မျက်မှန်ကို တပ်လိုက်ပြီး ဤကျော်ကြားသော ပန်းအကြောင်းကို သင်ကြားလိုက်ပါ။",
  "title2": "နှင်းဆီ၏အဓိပ္ပါယ်များ",
  "description4": "နှင်းဆီနီ၊ ချွှဲဖတ်ပြာဆိုတာလား? တကယ်တော့ မဟုတ်ဘူး။ နှင်းဆီတွေမှာ ဖြူ၊ ပန်းရောင်၊ နုရောင်၊ ခရမ်းရောင်၊ အဝါရောင်၊ လိမ္မော်ရောင်၊ မည်းရောင်... ဟုတ်လား? မည်းရောင်လည်းရှိတာလား? နှင်းဆီရောင်များ၏အဓိပ္ပါယ်များအကြောင်း ဗဟုသုတပြည့်စုံသော စာအုပ်များတောင် ရေးထားကြသည်။ တစ်နိုင်ငံမှာ သံယောဇဉ်ကိုဖော်ပြသည့် နှင်းဆီသည် တစ်နိုင်ငံတွင် နာကြည်းမှုကိုဖော်ပြနိုင်သည်။ ရာစုနှစ်များစွာ ဆက်လက်ပြောဆိုလာသည့် သင်္ကေတဓလေ့များထဲမှ အနည်းငယ်သာ ယခုမှတ်ယူကြည့်ကြပါ။"
  , "title3": "နှင်းဆီရောင်များအလိုက် အဓိပ္ပါယ်များ",
  "description5": "အနီရောင်နှင်းဆီများသည် အချစ်၏သင်္ကေတဖြစ်သည်။ (တစ်သန်းချီသော တက်တူးများမှားနေမည်မဟုတ်ပါ။) ၎င်းသည် အတုယူမှုတစ်ခုဖြစ်နိုင်သော်လည်း နှလုံးခုန်သံကို မြန်စေသောသူတစ်ဦးထံမှ ရရှိသည့် နီရောင်နှင်းဆီကို လက်မခံသူကို မတွေ့ရသေးပါ။ဗစ်တိုးရီးယန်းလက်ရာအရ ဖြူရောင်နှင်းဆီများသည် အချစ်နှင့်မရင်းနှီးသည့်နှလုံးသား ကိုဖော်ပြသည်။ ၎င်းသည် လူငယ်ချစ်ခြင်းမေတ္တာနှင့်သန့်ရှင်းမှု ကိုဖော်ပြနိုင်သည့်အပြင် အေးစက်သောနှလုံးသား၏ တည်ငြိမ်မှု ကိုလည်း ကိုယ်စားပြုနိုင်သည်။နီနှင့်ဖြူ နှစ်ရောင်ပေါင်းစပ်ထားသည့် နှင်းဆီတစ်ခွက် သည် စည်းလုံးညီညွတ်မှု ကိုဖော်ပြသည်။ ယင်းသည် လန်ကက်စတာနွယ်ဖွားနှင့် ယော့ခ်နွယ်ဖွားတို့၏သင်္ကေတကို ဖော်ပြသကဲ့သို့ အလယ်ခေတ်တွင် မျိုးဆက်အဆက် ပြုစုပျိုးထောင်လာသည့် ယှဉ်ပြိုင်မှုများကို မျိုးဆက်သစ်၏ အိမ်ထောင်ရေးဖြင့် ပြေလည်ခဲ့သည်။ပန်းရောင်နှင်းဆီများသည် မည်သည့်အခြေအနေမျိုးမဆို သင့်တော်သည်။ ၎င်းသည် ကျေးဇူးတင်မှု၊ တန်ဖိုးထားမှု၊ လှုံ့ဆော်မှုနှင့် ငယ်မြူမှု ကိုဖော်ပြနိုင်သည်။ အသားရောင်ပန်းရောင်နှင်းဆီသည် သန့်ရှင်းမှုနှင့်သည်းခံမှု ကိုဖော်ပြပြီး သနားမှုဖော်ပြလိုပါကလည်း သင့်တော်သည်။အသံကျယ်သော ပန်းရောင်နှင်းဆီများသည် လူတစ်ဦးဦး၏ စိတ်ဝင်စားမှုကို ဖော်ပြခြင်း ဖြစ်သည်။ ပျော်ရွှင်မှုနှင့် ပျော်စရာကောင်းသော ခံစားမှုများ ကိုဖော်ပြလိုပါက သင့်တော်သည်။ထူးခြားစွာ တောက်ပသည့် ပန်းရောင်နှင်းဆီများ သည် မိတ်ဆွေအတွက် အားထားမှုနှင့် ဂရုစိုက်မှု ကိုဖော်ပြသည်။ အထူးသဖြင့် မိခင်နေ့တွင် မိခင်ဆုံးရှုံးသည့်သူများအတွက် သင်္ကေတတစ်ခုဖြစ်နိုင်သည်။အနက်ရောင်နှင်းဆီများ သည် အဆုံးသတ်ခြင်းနှင့် အသစ်တစ်ခုစတင်ခြင်း ကိုဖော်ပြသည်။ခရင်မ်ရောင်နှင်းဆီများ သည် စဉ်းစားတုံ့တွေးမှု နှင့်သက်တောင့်သက်သာမှုကို ကိုယ်စားပြုသည်။နုလျှောသော လိမ္မော်ရောင်နှင်းဆီများ သည် ရိုးရွင်းမှု ကိုဖော်ပြပြီး ဆာမွန်ရောင်နှင်းဆီများ သည် တောင်းဆိုမှုနှင့် လိုချင်မှု ကိုဖော်ပြသည်။"
  ,"title4" : "ဇွန်လ၏ သင်္ကေတပန်း"
  , "title5": "နှင်းဆီနှင့်သမိုင်း",
  "description6": "သံခဲမြေဆီထွက်များအရ နှင်းဆီသည် ၃၅ သန်းနှစ် ခန့်ကတည်းက တည်ရှိခဲ့ပြီး ၅,၀၀၀ နှစ်ကျော် ကတည်းက လူတို့မွေးမြူခဲ့ကြသည်။ ယခုအခါ နှစ်စဉ်အမေရိကန်တွင် <br> ရောင်းချသော နှင်းဆီ ၁.၅ ဘီလီယံ၏ များစုသိပ်မှု သည် ကိုလံဘီယာနှင့် အက္ကွေဒေါမှ ရလာသည်။တရုတ်မှ လက်ဖက်နှင်းဆီများ၊ ပြင်သစ်မှ ဘောဘွန်နှင်းဆီများ နှင့် သမိုင်းဝင်အမေရိကန် American Beauty နှင်းဆီတို့သည် ထင်ရှားသည်။ အမေရိကန်၏ နိုင်ငံတော်မြို့တော် District of Columbia ၏ တရားဝင်ပန်း ဖြစ်သည့်အပြင် Grateful Dead ဂီတအယ်လ်ဘမ် တစ်ခုနှင့် သရုပ်ဆောင်ဆုရထားသော ရုပ်ရှင်တစ်ခု ထဲတွင်ပါ ပါဝင်သည်။နှင်းဆီသည် ဇွန်လ၏ မွေးသက္ကရာဇ်ပန်း ဖြစ်သော်လည်း ဗယ်လင်တိုင်းနေ့ နှင့် မိခင်နေ့ တွင် အမေရိကန်တွင် အရောင်းအလွန်များသည်။နှင်းဆီပွဲတော် (Rose Parade) သည် နယူးယားနှစ်ကူးနေ့ပွဲ အဖြစ် Pasadena, California တွင် ၁၈၉၀ ခုနှစ်မှစ၍ သင်္ဘော float များကို နှင်းဆီသန်းနဲ့ချီ အသုံးပြု၍ အလှဆင်သော ပွဲတစ်ခုဖြစ်သည်။ရောမနောက်ကွယ်မှ နှင်းဆီပုံပြင်များအင်ပါယာ နီရို သည် သူ၏ ဧည့်ခံပွဲများတွင် နှင်းဆီပွင့် တန်ချီသွန်းချခဲ့သည်။ကလီယိုပတ်ထရာ သည် ရောမစစ်သူကြီး Mark Antony ကို မိမယ်ဖို့ သူ့အိမ်တော်တွင် နှင်းဆီနဲ့ပြည့်အောင် ပြင်ဆင်ခဲ့သည်။သူမသည် ရေကူးသင်္ဘော sails များကို နှင်းဆီရေနံဖြင့်စိမ်ပြီး နူးညံ့မွှေးကြိုင်မှုဖြင့် သူ့ရောက်ရှိမှုကို ကြေငြာခဲ့သည် နှင်းဆီ၏ အသုံးချမှုများနှင်းဆီဖရဲခွန် (Rosehip) လက်ဖက်ရည် သည် ဗီတာမင် C ကြွယ်ဝမှု ကြောင့် ကျန်းမာရေးကောင်းမွန်စေသည်။နှင်းဆီရေနံ သည် Dior, Balenciaga, Prada ကဲ့သို့ ဖရန်ဂရန်ซ์အမှတ်တံဆိပ်များ ထဲတွင် အရေးပါသော ဆော့ဗျူးဖြစ်သည်။နှင်းဆီရေ သည် ဘက်လဗား၊ ဟယ်လဗာ ကဲ့သို့ အရှေ့တိုင်းမုန့်များ ထဲတွင် ပါဝင်သည်။နှင်းဆီနှင့် သံသရာသဘာဝတွင် နှင်းဆီသည် အလွန်စုံလင်သောမွှေးကြိုင်မှု ရှိသော်လည်း သစ်စေ့ပျိုးသူများသည် အနံ့ထက် အရောင်အသစ်များနှင့် တည်ကြယ်မှုကို ပိုမိုစဉ်းစားကြသည်။ထို့ကြောင့် Leonidas နှင်းဆီကဲ့သို့ အနံ့လုံးဝမရှိသော နှင်းဆီများ လည်းရှိသည်။ နှင်းဆီနှင့်ပတ်သက်သော သီချင်းများစွာ ရှိသည်။မာနမှုနှင့်ဝမ်းနည်းမှုကိုဖော်ပြသော Poison ၏  သည် စိတ်ဝင်စားစရာကောင်းသည်။နှင်းဆီသည် သမိုင်း၊ ယဉ်ကျေးမှု၊ ခံစားမှုနှင့် အလှတရား နှင့် မျှတစွာ ဆက်စပ်နေသော သက်တမ်းရှည်သည့် ပန်းဖြစ်သည်။ "
  , "title6": "ပန်းများကိုစောင့်ရှောက်ခြင်း",
  "description7": "နှင်းဆီများကို သန့်ရှင်းပြီး နှစ်ပေါင်းနှစ်များအထိ သန်စွမ်းစွာ ထိန်းသိမ်းရခြင်းမှာ ကြီးမားသော လျှို့ဝှက်ချက်မရှိပါ။ အခြားတစ်ခုမှာ နှင်းဆီများကို သင်ယူခဲ့သောအချိန်မှာ ကုလားပင်များတည်ရှိခဲ့သည့် အလယ်အာမေရိကတွင် ၂ လကြာပြီး အပူအေးသုံးညီသော ပတ်ဝန်းကျင်ထဲသိုလှောင်ပြီး ပြန်လည်ပို့ဆောင်မည့်အထိ သာလွန်အောင် ထိန်းသိမ်းထားသည်ဟုဆိုနိုင်ပါသည်။ တင်သွင်းပြီးသည့် နှင်းဆီများကို အိမ်သို့တင်သွင်းလာပြီးပါက, သင်၏တစ်ဘူးတစ်ခွက်ပါ၀င်သော သက်ဆိုင်ရာပန်းရိုက်ဆီအမှတ်များက မီးရထားရှိတဲ့ရေအောက်မှာတင်ဖုံးခွင့်ပေးမဲ့ အရွက်များကို ဖယ်ရှားပေးရမည်။ ရေအတွင်း အသားခံအပူအောက်သာဖြင့် ပန်း၏ထူးချွန်ပြုပြင်ရေးဗျာ အသုံးများပါသော ပေါက်ဆစ်ခြင်းကော်ပြစ်လျှော့ပါ။"
  //"description3":
  //"description3":
  //"description3": 
}
    };
});
