<html>
<p align="left"><b>TECHNICAL-TEST</b></p>
<p><strong>Answer of General Questions</strong></p>
<body>
    <p align=justify>•I consider that the most critical metrics to monitor the system are those of performance, both from the virtual Java machine (JVM) and from the database (MongoDB).<br>
    I would use tools such as ManageEngine Applications Manager, because it allows monitoring the performance of servers and necessary applications, which helps to ensure high availability and optimal performance, ensuring high uptime. And also, it allows you to act quickly to solve problems.</p>
    <p>•The command is:<br>
    <ul>
          find . -type f -atime +20 -print<br>
          find . -type f -atime +20 -delete<br>
          find . -type f -atime +20 -exec rm {} \;</p>
    </ul>
    <p>The <b>find</b> command allows us to find files with certain conditions.</p>
    <ul>
    <p><b>. =</b> It is the path where it will be searched, in this case in the current directory; you can also use another /mnt path. It is recommended to use the absolute path.<br>
       <b>-type f =</b> Specifies the type of file, in this case "f" indicates file.<br>
       <b>-atime =</b> Access Time, allows you to search for files according to the time of the last access.<br>
       <b>+20 =</b> Indicates that files with more than 20 days of last access are searched.<br>
       <b>-print =</b> Prints the full path of the files found on the screen. It is recommended to use this command first to make sure you want to delete such information.<br>
       <b>-delete =</b> Indicates to delete files that meet the parameters.<br>
       <b>-exec rm =</b> Allows you to launch a command on the results, for example, <b>rm</b>.<br>
       <b>{} \; =</b> It is specified to close the command.</p>
    </ul>
    <p>Both the <b>-delete</b> and the <b>-exec rm</b> parameters can delete the files.
</body>
</html>
