<?php
$files=glob("C:/xampp/htdocs/wariyum/experimentdirectory/*.csv");
foreach($files as $file){
    if(($handle=fopen($file,"r"))!==FALSE){
        echo "<b>filename:".basename($file)."</b><br><br>";
        while(($data=fgetcsv($handle,4096,","))!==FALSE){
            echo implode("\t",$data);

        }
        echo "<br>";
        fclose($handle);
    }
    else{
        echo "couldn't open file".$file;
    
    }
}
?>