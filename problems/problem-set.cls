\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{problem-set}

\LoadClass[12pt]{article}

\RequirePackage{graphicx} % Allows for eps images
\RequirePackage[dvips,letterpaper,margin=1in,bottom=0.7in]{geometry}
\RequirePackage{tensor}
\RequirePackage{ifthen}

 % Sets margins and page size
\RequirePackage{xcolor}
\RequirePackage[framemethod=TikZ]{mdframed}
\RequirePackage[utf8]{inputenc}	
\RequirePackage[T1]{fontenc}

% \usepackage{mathpazo} % Use the Palatino font by default
\RequirePackage{parskip}
\RequirePackage{relsize}
\RequirePackage{xifthen}
\RequirePackage{fontawesome}
\RequirePackage{amsthm} % Theorem Formatting
\RequirePackage{amssymb}    % Math symbols such as \mathbb
\RequirePackage{amsmath}
    
\RequirePackage{interval}

% ************* Options ****************
\newif\ifshowauthor

\DeclareOption{showauthor}{%
    \showauthortrue
}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

% ************* Problem formatting helpers ****************

\newcommand{\difficulty}[1]{\noindent\textbf{Difficulty}: #1\\[\baselineskip]}

\newlength{\rulelength}
\newcommand{\inputformat}{\vspace{\baselineskip}\par\noindent\textbf{Input Format}\\[0.2\baselineskip]}
    
\newcommand{\constraints}{\vspace{\baselineskip}\par\noindent\textbf{Constraints}\\[0.2\baselineskip]}
\newcommand{\outputformat}{\vspace{\baselineskip}\par\noindent\textbf{Output Format}\\[0.2\baselineskip]}
    
\newcommand{\addsample}[2]{\begin{sample}{\par\noindent\textbf{Input}\\[0.2\baselineskip]\texttt{#1}}\vspace{0.5em}\\\setlength{\rulelength}{\textwidth}\addtolength{\rulelength}{2em}\hspace*{-1em}\noindent{\rule{\rulelength}{0.4pt}}{\par\noindent\textbf{Output}\\[0.2\baselineskip]\texttt{#2}}\end{sample}}
    
\newcommand{\addsampleExplanation}[3]{\begin{sample}{\par\noindent\textbf{Input}\\[0.2\baselineskip]\texttt{#1}}\vspace{0.5em}\\\setlength{\rulelength}{\textwidth}\addtolength{\rulelength}{2em}\hspace*{-1em}\noindent{\rule{\rulelength}{0.4pt}}{\par\noindent\textbf{Output}\\[0.2\baselineskip]\texttt{#2}}
\\\setlength{\rulelength}{\textwidth}\addtolength{\rulelength}{2em}\hspace*{-1em}\noindent{\rule{\rulelength}{0.4pt}}{\par\noindent\textbf{Explanation}\\[0.2\baselineskip]#3}\end{sample}}
    
\mdfdefinestyle{problemstyle}{frametitlerule=true,frametitlebackgroundcolor=gray!20,innertopmargin=\topskip,skipabove=2cm,leftmargin=1em,rightmargin=1em}
\mdtheorem[style=problemstyle]{problem}{Problem}
\mdfdefinestyle{samplestyle}{frametitlerule=true,frametitlebackgroundcolor=gray!20,innertopmargin=\topskip,innerleftmargin=1em,innerrightmargin=1em,outerlinecolor=gray!20!gray!20,outerlinewidth=0.4pt,innerbottommargin=0.8em}
\mdtheorem[style=samplestyle]{sample}{Sample}
\renewcommand\thesample{\Roman{sample}}
    
\newcommand{\notewarning}[1]{\faWarning\, \textbf{Note:} #1}
\newcommand{\nextpagesign}{\notewarning{The problem specification continues on the next page.}}
\newcommand{\pushnewpage}
{
    \vfill
    \nextpagesign
    \newpage
}

\let\@subheader\@empty
\newcommand{\subheader}[1]{\gdef\@subheader{#1}}

\renewcommand\maketitle{
    {\noindent\fontseries{b}\fontsize{24}{30}\selectfont\@title}
    \\[2\baselineskip]
    {{\bf\@subheader}\\
    {\textit{\@date}}}\ifshowauthor\hfill\hfill{\large{\@author}}\fi
    \vspace{1em}
    \hrule
}

\@addtoreset{sample}{section}