<?php
function wiktionary_lookup($word){
    $data = get_data('https://en.wiktionary.org/wiki/'.$word);
    $pos = strpos($data, "<span class=\"mw-headline\" id=\"Etymology");
    $etym = substr($data, strpos($data, "<p>", $pos)+3, strpos($data, "<h3>", $pos)-strpos($data, "<p>", $pos)-3);
    while(strpos($etym, "mention\" lang=")){
       // code = etym[etym.find("lang=", etym.find("mention\" lang="))+6:etym.find(">", etym.find("mention\" lang="))-1]
        $code = substr($etym, strpos($etym, "lang=", strpos($etym, "mention\" lang="))+6, strpos($etym, ">", strpos($etym, "mention\" lang="))-strpos($etym, "lang=", strpos($etym, "mention\" lang="))-7);
        //etym = etym[etym.find("mention\" lang=")+1:]
        echo $code;
        echo "<br>";
        $etym = substr($etym, strpos($etym, "mention\" lang=")+1);
    }
}

// you can add anoother curl options too
// see here - http://php.net/manual/en/function.curl-setopt.php
function get_data($url){
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36");
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($ch, CURLOPT_SSL_VERIFYHOST,false);
  curl_setopt($ch, CURLOPT_SSL_VERIFYPEER,false);
  curl_setopt($ch, CURLOPT_MAXREDIRS, 10);
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
  //curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
  $data = curl_exec($ch);
  curl_close($ch);
  return $data;
}

$output = wiktionary_lookup("word");
//echo strlen($output);
?>
