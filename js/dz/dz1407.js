document.writeln('<table border="1" width="260">');
document.writeln('<tr align="center">');
for (let i =0; i < 11; i++){
    document.writeln('<td>' + i + '</td>')
}
document.writeln('</tr>')
for(let i=1; i < 11; i++){
    document.writeln('<tr align="center">');
    document.writeln('<td>' + i + '</td>')
    for(let j=1; j < 11; j++){
        if(i%2 != 0){
            if(j%2 != 0){
            document.writeln('<td bgcolor="red">' + i * j + '</td>');
            } else{
            document.writeln('<td bgcolor="yellow">' + i * j + '</td>');
        }
            }else{
                if(j%2 == 0){
            document.writeln('<td bgcolor="red">' + i * j + '</td>');
            } else{
            document.writeln('<td bgcolor="yellow">' + i * j + '</td>');
        }
            }
    }
    document.writeln('</tr>');
}
document.writeln('</table>');