\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cslesson}
\LoadClass{article}

\RequirePackage[svgnames]{xcolor}
\RequirePackage[dvips,letterpaper,margin=1in,bottom=0.7in]{geometry}
\RequirePackage{helvet}
\RequirePackage{titlesec}
\RequirePackage{fancyhdr}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\cfoot{\textit{``Dedicated to Papa Smurf''}}
\rfoot{\thepage}

% ************* Options ****************
\newif\ifprereq

\DeclareOption{prereq}{%
    \prereqtrue
}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

% ************* Title formatting ****************

\newcommand{\titlehrule}{{\color{DarkGoldenrod}\rule{1\linewidth}{1pt}}}

\renewcommand{\maketitle}{
    \noindent
    \ifprereq
    \begin{flushright}
    {\footnotesize\slshape\sffamily{Prerequisite Lesson}}
    \end{flushright}
    \vspace{-3ex}
    \fi
    \titlehrule
    \vspace{2ex}
    \par
    \noindent
    \begin{minipage}{0.65\linewidth}
        \begin{flushleft}
            {\par\bfseries\sffamily\fontsize{30}{30}\color{DarkRed}\selectfont\@title\par}
        \end{flushleft}
    \end{minipage}
    
    \vspace{4ex}
    \noindent
    \begin{minipage}{0.65\linewidth}
        \begin{flushleft}
            {\large \lineskip 0.5em \bfseries\scshape\sffamily\@author}
            {\footnotesize\slshape\sffamily\hspace{5pt} \@date \par}
        \end{flushleft}
    \end{minipage}
    \par
    \vspace{3ex}
    \noindent
    \titlehrule
    \vspace{3ex}
}

% ************* Chapter and section formatting ****************
\titleformat{\chapter}[display]
  {\normalfont\sffamily\huge\bfseries\color{blue}}
  {\chaptertitlename\ \thechapter}{20pt}{\Huge}
\titleformat{\section}
  {\normalfont\sffamily\Large\bfseries}
  {\thesection}{1em}{}
