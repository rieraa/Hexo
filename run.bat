call hexo clean

:: 检查第一个命令是否成功执行
if %errorlevel%==0 (
    :: 如果第一个命令成功执行，执行第二个命令 hexo g
    call hexo g

    :: 检查第二个命令是否成功执行
    if %errorlevel%==0 (
        :: 如果第二个命令成功执行，执行第三个命令 hexo d
        call hexo s
    ) else (
        echo 第二个命令执行失败
    )
) else (
    echo 第一个命令执行失败
    echo 详细错误信息：%errorlevel%
)

pause
