[Last update Dec 2022]
# Time Series Analysis and Financial Engineering With Python
This is a compound course on time series analysis, financial engineering and algorithmic trading featuring Python programming. Originally it was for night training sessions for new-hire in my previous institution (hedge fund), all quantitative analysts and macro analysts are supposed to have more than working knowlege of time series modelling, so this training session will discuss and demonstrate the underlying mathematical foundations, modelling and Python-related skills. 

The tutorial splits in several parts, the Part I discusses various topics in time series analysis, the Part II will cover the classic financial engineering, the Part III discusses portfolio optimization and management, the Part IV discusses systematic trading. Also there are some supplementary tutorials about algorithms and data structures as a starter reference for more complicated quant developing topics. 

All learners are required to have solid knowledge of <a href='https://github.com/MacroAnalyst/Linear_Algebra_With_Python'>linear algebra</a>, <a href='https://github.com/MacroAnalyst/Probability_Theory'>probability theory</a>, <a href='https://github.com/MacroAnalyst/Basic_Statistics_With_Python'>statistics</a> and <a href='https://github.com/MacroAnalyst/Basic_Econometrics_With_Python'>basic econometrics</a>. All analysts are researchers too, with these knowledge, you can freely read institutional or academic researches and internalize them into your own analystical framework.

## Prerequisites
The learners must have working knowledge of linear algrebra, statistics and probability theory, and ideally advanced econometrics skills too.

And also the learners are assumed to have constant exposure of

- [x] Python
- [x] NumPy
- [x] Matplotlib
- [x] Statsmodels
- [x] Pandas

## Environment Setup
I use poetry to management environment, if you happen to use VS code like me, please follow the steps below:
1. In Windows powershell and install poetry ``` (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -p```
2. Navigate to ```cd $env:APPDATA\Python\Scripts```, check if poetry being installed.
3. Open a notepad ```notepad $profile``` and set alias for poetry ```Set-Alias poetry "C:\Users\user\AppData\Roaming\Python\Scripts\poetry.exe"``` in notepad, I prefered this way, because sometimes setting env path not working in windows.
4. Reload profile by ```. $profile```.
5. If you are on your personal computer ```Set-ExecutionPolicy RemoteSigned -Scope CurrentUser``` to unstrict your execution policy and choose Y.
6. Resume the default restricted policy for security ```Set-ExecutionPolicy Restricted -Scope CurrentUser```.
7. Now check ```poetry --version```, if you see the version printed, then means we succeed in setting alias.
8. You choose to use ```poetry update```, or just manage version at your own convenience.
9. Download python 3.12 or anything version higher ```Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe" -OutFile "python-3.12.0-amd64.exe"```.
10. This command will install python ```Start-Process -FilePath ".\python-3.12.0-amd64.exe" -ArgumentList "InstallAllUsers=1 PrependPath=1" -Wait```.
11. According to my installed directory, we will let poetry to use the newly installed Python ```poetry env use "C:\Program Files\Python312\python.exe"```.
12. Enter ```poetry shell```, check ```python --version```.
13. Do ```poetry install```, this should create poetry.lock accoring to poetry toml.
14. ```poetry run python -m ipykernel install --user --name=poetry-env --display-name "Python (Poetry)"``` will register and create Jupyter kernel.
15. ```poetry env info -p``` will print out the path of this kernel.
16. Give this path to "Select Python Interpretor" menu.

## Contents
It is advised that you download all material and browse in your own computer, since nbviewer has persistent LaTeX rendering errors.
### Part I
[Chapter 0 - Dates and Time in Python](https://nbviewer.org/github/weijie-chen/Time-Series-Analysis-With-Python/blob/main/Chapter%200%20-%20Dates%20And%20Time%20In%20Python.ipynb)<br>
[Chapter 1 - Time Series Manipulation](https://nbviewer.org/github/weijie-chen/Time-Series-Analysis-With-Python/blob/main/Chapter%201%20-%20Time%20Series%20Manipulation.ipynb)<br>
[Chapter 2 - Lag Operator and Difference Equation](https://nbviewer.org/github/weijie-chen/Time-Series-Analysis-With-Python/blob/main/Chapter%202%20-%20Lag%20Operator%20and%20Difference%20Equations.ipynb)<br>
[Chapter 3 - Simple and Log Returns](https://nbviewer.org/github/weijie-chen/Time-Series-Analysis-With-Python/blob/main/Chapter%203%20-%20Simple%20and%20Log%20Returns.ipynb)<br>
[Chapter 4 - Stationary Processes and Trend Removal](https://nbviewer.org/github/weijie-chen/Time-Series-Analysis-With-Python/blob/main/Chapter%204%20-%20Stationary%20Processes%20and%20Trend%20Removal.ipynb)<br>
[Chapter 5 - ARMA Models](https://nbviewer.org/github/weijie-chen/Time-Series-Analysis-With-Python/blob/main/Chapter%205%20-%20ARIMA%20models.ipynb)<br>
[Chapter 6 - ARCH and GARCH Models](https://nbviewer.org/github/weijie-chen/Time-Series-and-Financial-Engineering-With-Python/blob/main/Chapter%206%20-%20ARCH%20and%20GARCH.ipynb)<br>
[Chapter 16 - Implementing Technical Indicators](https://nbviewer.org/github/weijie-chen/Time-Series-and-Financial-Engineering-With-Python/blob/main/Chapter%2016%20-%20Implementing%20Technical%20Analysis.ipynb)<br>

### Part II
[Chapter 0 - Wiener Process and Random Walk](https://nbviewer.org/github/weijie-chen/Time-Series-and-Financial-Engineering-With-Python/blob/main/Chapter%200%20-%20Dates%20And%20Time%20In%20Python.ipynb)<br>
[Chapter 1 - Bond Valuation and Modern Portfolio Theory](https://nbviewer.org/github/weijie-chen/Time-Series-and-Financial-Engineering-With-Python/blob/main/FinEng%20Chapter%201.%20Bond%20and%20Modern%20Portfolio%20Theory.ipynb)<br>
[Chapter 2 - Capital Assets Pricing Model (CAPM)](https://nbviewer.org/github/weijie-chen/Time-Series-and-Financial-Engineering-With-Python/blob/main/FinEng%20Chapter%202%20-%20CAPM.ipynb)<br>
[Chapter 3 - Options Pricing](https://nbviewer.org/github/weijie-chen/Time-Series-and-Financial-Engineering-With-Python/blob/main/FinEng%20Chapter%203%20-%20Options.ipynb)<br>
[Chapter 4 - Rates Modeling](https://nbviewer.org/github/weijie-chen/Time-Series-and-Financial-Engineering-With-Python/blob/main/FinEng%20Chapter%204%20-%20Rates%20Modelling.ipynb)<br>
[Chapter 5 - Value at Risk (VaR)](https://nbviewer.org/github/weijie-chen/Time-Series-and-Financial-Engineering-With-Python/blob/main/FinEng%20Chapter%205%20-%20Value%20at%20Risk%20%28VaR%29.ipynb)<br>


## Screen Captures
![opt](https://user-images.githubusercontent.com/59842360/210231047-e4b55f54-3e7c-419a-a8a5-60b55e3a35db.jpg)
![capm](https://user-images.githubusercontent.com/59842360/210231049-7d8357a2-9994-43f3-b060-968f6c10d1dd.jpg)
![simu](https://user-images.githubusercontent.com/59842360/210231051-8be2bdaf-8859-4bf4-b5ad-67a7be1d8634.jpg)
![ou](https://user-images.githubusercontent.com/59842360/210231052-7167e552-3dcd-4268-9a3f-f5967f69772c.jpg)
![mpt](https://user-images.githubusercontent.com/59842360/208608006-a768764a-a27f-406a-92ad-b93c967bf65f.jpg)
![rolling_mean](https://user-images.githubusercontent.com/59842360/208608011-e809831c-6064-4d0b-9605-83411e2c2697.jpg)
![AR](https://user-images.githubusercontent.com/59842360/208608014-1987f121-8c38-4e23-8306-58aa80dd715a.jpg)
![IRF](https://user-images.githubusercontent.com/59842360/208608019-c085a92b-7f0d-42b2-a7dd-6cef98eb5225.jpg)
![log_division](https://user-images.githubusercontent.com/59842360/208608314-263ef029-dd1e-4ee1-b51d-0173a5c92c0e.jpg)
![fx_dist](https://user-images.githubusercontent.com/59842360/208608022-7b39827f-2972-45e9-8c9c-d15fc03ed5a1.jpg)
![sp500](https://user-images.githubusercontent.com/59842360/208608024-1d824637-9458-49c4-a7bc-7b7da1778513.jpg)
![diag](https://user-images.githubusercontent.com/59842360/208608026-94e124d4-257d-41fd-b7c5-ef0c9fbd44e2.jpg)

