%% concrete-book.cls
%% Copyright 2018 Shon Verch
%
% This work may be distributed and/or modified under the
% conditions of the LaTeX Project Public License, either version 1.3
% of this license or (at your option) any later version.
% The latest version of this license is in
%   http://www.latex-project.org/lppl.txt
% and version 1.3 or later is part of all distributions of LaTeX
% version 2005/12/01 or later.
%
% This work has the LPPL maintenance status `maintained'.
% 
% The Current Maintainer of this work is Shon Verch.
%
% This work consists of the files concrete-book.cls
% and the derived file main.tex

% Theorem styling is from Legrand Orange Book Template

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{concrete-book}

\LoadClass{scrbook}
\RequirePackage{geometry}
\RequirePackage[calcwidth]{titlesec}
\RequirePackage{calc}
\RequirePackage{marginnote}
\RequirePackage{changepage}
\RequirePackage[T1]{fontenc}
\RequirePackage{helvet}
\RequirePackage{fancyhdr}
\RequirePackage{titletoc}
\RequirePackage{xcolor}
\RequirePackage{pgffor}
\RequirePackage{tikz}

% Define the orange color used for highlighting throughout the book
% 243,102,25
\definecolor{accent}{RGB}{0,0,0} 

% Set koma font to use computer modern family.
\addtokomafont{disposition}{\rmfamily}
\addtokomafont{chapter}{\rmfamily}
\addtokomafont{chapterentry}{\rmfamily}

% Document geometry
\newgeometry{top=2.1cm, bottom=2.1cm, inner=4.3cm, outer=2.2cm, 
    footskip=0.8cm, marginparsep=0.5cm, marginparwidth=2.8cm, reversemarginpar,
    headsep=0.6cm}
    
\savegeometry{content}

% Header and footer configuration
\pagestyle{fancy}

\newlength{\pagenumerboxlen}
\newcommand{\recalcPagenumerboxlen}{\setlength{\pagenumerboxlen}{0.4cm + \widthof{\thepage}}}

\newcommand{\rpagenumerbox}{\rlap{\mbox{\hspace{0.4cm}\thepage}}}
\newcommand{\lpagenumerbox}{\recalcPagenumerboxlen\hspace{-\pagenumerboxlen}\makebox[\pagenumerboxlen][l]{\thepage}}

\cfoot{}
\fancyhead{}
\fancyhead[RO]{\rightmark\rpagenumerbox}
\fancyhead[LE]{\lpagenumerbox\leftmark}

\renewcommand{\headrulewidth}{0pt}

\renewcommand{\chaptermark}[1]{%
 \markboth{\textbf{\MakeUppercase{#1}}}{\textbf{\MakeUppercase{#1}}}%
}

\renewcommand{\sectionmark}[1]{%
\markright{\textbf{\MakeUppercase{\thesection\ #1}}}}

%----------------------------------------------------------------------------------------
%	CHAPTER FORMATTING
%----------------------------------------------------------------------------------------
\newcommand{\lmr}{\fontfamily{lmr}\selectfont} % Latin Modern Roman

\newlength\chapterrulelen
\setlength\chapterrulelen{\dimexpr\marginparwidth+\marginparsep+\hoffset\relax}

\titleformat{\chapter}[display]
    {\normalfont\Huge\bfseries\justifyifodd}
    {\lmr\fontsize{86}{0}\selectfont \thechapter}
    {2.6cm}{}
    [\if@mainmatter\vspace{-1.5ex}{\makebox[\linewidth][l]{%
    \hspace*{-\chapterrulelen}\rule{\dimexpr\textwidth+\chapterrulelen\relax}{0.5pt}}}\fi]

\titlespacing*{\chapter}
  {0pt}
  {0pt}
  {\if@mainmatter{2ex}\else{3.5ex}\fi}
  
%----------------------------------------------------------------------------------------
%   PART FORMATTING
%----------------------------------------------------------------------------------------
% TODO: Centre part header and make it look nicer.
 
%----------------------------------------------------------------------------------------
%   TOC FORMATTING
%----------------------------------------------------------------------------------------
\KOMAoptions{toc=chapterentrydotfill}

%----------------------------------------------------------------------------------------
%	PART COMMAND WITH CUSTOM GEOMETRY LOGIC
%----------------------------------------------------------------------------------------
\let\oldpart\part
\renewcommand{\part}[1]
{
    \restoregeometry
    \oldpart{#1}
    \loadgeometry{content}
}

\newcommand{\justifyifodd}{}

\let\oldmainmatter\mainmatter
\renewcommand{\mainmatter}
{
    \oldmainmatter
    \loadgeometry{content}
    \renewcommand{\justifyifodd}{
        \checkoddpage
        \ifoddpage\raggedleft\else\fi
    }
    
    \setcounter{page}{1}
    
    % A possible fix to the marginnote page count
    % issue if it shall arise again. This sets the
    % internal page counter in the marginnotes
    % package to page 1.
    % \gdef\themn@abspage{1}
}

%----------------------------------------------------------------------------------------
%	MARGIN NOTES CONFIGURATION
%----------------------------------------------------------------------------------------
\renewcommand*{\marginfont}{\noindent\small\slshape}
\renewcommand*{\raggedleftmarginnote}{\raggedrightmarginnote}

%----------------------------------------------------------------------------------------
%	TITLE PAGE
%----------------------------------------------------------------------------------------
\newcommand{\makesimpletitle}{%
    \vspace*{20ex}
    {\sffamily\fontsize{40}{48}\bfseries\@title}
    \vskip 6ex
    {\huge\ifdefedition\sffamily{\@edition}\else\bfseries\@subtitle\fi}
    \ifx\@dedication\@empty \else
    \vfill
    {\LARGE\itshape\@dedication}
    \fi
}

\newif\ifdefedition
\let\@edition\@empty
\newcommand{\edition}[1]{\gdef\@edition{#1}\defeditiontrue}

\newcommand{\titleauthorformat}[1]{\MakeUppercase{#1}}

\newcommand{\makecomplextitle}{%
    \vspace*{20ex}
    {\sffamily\fontsize{40}{48}\bfseries\@title}
    
    \vskip 6ex
    
    \ifx\@subtitle\@empty \else
    \parbox{\textwidth}{%
        {\huge\bfseries\@subtitle\par}
    }
    
    \vskip 6ex
    \fi


    \ifx\@subtitle\@empty
    {\sffamily\huge\@edition}
    \vskip 6ex 
    \else
    {\sffamily\LARGE\@edition}
    \fi
    
    \vskip 4cm
    \foreach \name in \@author {%
        {\edef\tmp{\noexpand\titleauthorformat{\name}}{\sffamily\large\tmp}\par\vspace{1.5ex}}
    }
}

\renewcommand{\maketitle}{%
    \cleardoubleoddpage
    \pagenumbering{gobble}

    \newgeometry{left=3cm, right=3cm, bottom=3cm, top=3cm}
    \pagestyle{empty}
    \makesimpletitle
    \cleardoubleoddpage
    \makecomplextitle
    \restoregeometry
    
    \pagestyle{fancy}
    \cleardoubleoddpage
    \pagenumbering{roman}
}

\newcommand{\newthought}[1]{\MakeLowercase{\textsc{#1}}}

%----------------------------------------------------------------------------------------
%	THEOREM STYLES
%----------------------------------------------------------------------------------------

\RequirePackage{amsmath} % For math equations, theorems, symbols, etc
\RequirePackage{amsfonts}
\RequirePackage{amssymb}
\RequirePackage{amsthm}

\newcommand{\intoo}[2]{\mathopen{]}#1\,;#2\mathclose{[}}
\newcommand{\ud}{\mathop{\mathrm{{}d}}\mathopen{}}
\newcommand{\intff}[2]{\mathopen{[}#1\,;#2\mathclose{]}}
\newtheorem{notation}{Notation}[chapter]

% Boxed/framed environments
\newtheoremstyle{ocrenumbox}% % Theorem style name
{0pt}% Space above
{0pt}% Space below
{\normalfont}% % Body font
{}% Indent amount
{\small\bfseries\sffamily\color{accent}}% % Theorem head font
{\;}% Punctuation after theorem head
{0.25em}% Space after theorem head
{\small\sffamily\color{accent}\thmname{#1}\nobreakspace\thmnumber{\@ifnotempty{#1}{}\@upn{#2}}% Theorem text (e.g. Theorem 2.1)
\thmnote{\nobreakspace\the\thm@notefont\sffamily\bfseries\color{black}---\nobreakspace#3.}} % Optional theorem note
\renewcommand{\qedsymbol}{$\blacksquare$}% Optional qed square

\newtheoremstyle{blacknumex}% Theorem style name
{5pt}% Space above
{5pt}% Space below
{\normalfont}% Body font
{} % Indent amount
{\small\bfseries\sffamily}% Theorem head font
{\;}% Punctuation after theorem head
{0.25em}% Space after theorem head
{\small\sffamily{\tiny\ensuremath{\blacksquare}}\nobreakspace\thmname{#1}\nobreakspace\thmnumber{\@ifnotempty{#1}{}\@upn{#2}}% Theorem text (e.g. Theorem 2.1)
\thmnote{\nobreakspace\the\thm@notefont\sffamily\bfseries---\nobreakspace#3.}}% Optional theorem note

\newtheoremstyle{blacknumbox} % Theorem style name
{0pt}% Space above
{0pt}% Space below
{\normalfont}% Body font
{}% Indent amount
{\small\bfseries\sffamily}% Theorem head font
{\;}% Punctuation after theorem head
{0.25em}% Space after theorem head
{\small\sffamily\thmname{#1}\nobreakspace\thmnumber{\@ifnotempty{#1}{}\@upn{#2}}% Theorem text (e.g. Theorem 2.1)
\thmnote{\nobreakspace\the\thm@notefont\sffamily\bfseries---\nobreakspace#3.}}% Optional theorem note

% Non-boxed/non-framed environments
\newtheoremstyle{ocrenum}% % Theorem style name
{5pt}% Space above
{5pt}% Space below
{\normalfont}% % Body font
{}% Indent amount
{\small\bfseries\sffamily\color{accent}}% % Theorem head font
{\;}% Punctuation after theorem head
{0.25em}% Space after theorem head
{\small\sffamily\color{accent}\thmname{#1}\nobreakspace\thmnumber{\@ifnotempty{#1}{}\@upn{#2}}% Theorem text (e.g. Theorem 2.1)
\thmnote{\nobreakspace\the\thm@notefont\sffamily\bfseries\color{black}---\nobreakspace#3.}} % Optional theorem note
\renewcommand{\qedsymbol}{$\blacksquare$}% Optional qed square
\makeatother

% Defines the theorem text style for each type of theorem to one of the three styles above
\newcounter{dummy} 
\numberwithin{dummy}{section}
\theoremstyle{ocrenumbox}
\newtheorem{theoremeT}[dummy]{Theorem}
\newtheorem{problem}{Problem}[chapter]
\newtheorem{exerciseT}{Exercise}[chapter]
\theoremstyle{blacknumex}
\newtheorem{exampleT}{Example}[chapter]
\theoremstyle{blacknumbox}
\newtheorem{vocabulary}{Vocabulary}[chapter]
\newtheorem{definitionT}{Definition}[section]
\newtheorem{corollaryT}[dummy]{Corollary}
\theoremstyle{ocrenum}
\newtheorem{proposition}[dummy]{Proposition}

%----------------------------------------------------------------------------------------
%	DEFINITION OF COLORED BOXES
%----------------------------------------------------------------------------------------

\RequirePackage[framemethod=default]{mdframed} % Required for creating the theorem, definition, exercise and corollary boxes

% Theorem box
\newmdenv[skipabove=7pt,
skipbelow=7pt,
backgroundcolor=black!5,
linecolor=accent,
innerleftmargin=5pt,
innerrightmargin=5pt,
innertopmargin=5pt,
leftmargin=0cm,
rightmargin=0cm,
innerbottommargin=5pt]{tBox}

% Exercise box	  
\newmdenv[skipabove=7pt,
skipbelow=7pt,
rightline=false,
leftline=true,
topline=false,
bottomline=false,
backgroundcolor=accent!10,
linecolor=accent,
innerleftmargin=5pt,
innerrightmargin=5pt,
innertopmargin=5pt,
innerbottommargin=5pt,
leftmargin=0cm,
rightmargin=0cm,
linewidth=4pt]{eBox}	

% Definition box
\newmdenv[skipabove=7pt,
skipbelow=7pt,
rightline=false,
leftline=true,
topline=false,
bottomline=false,
linecolor=accent,
innerleftmargin=5pt,
innerrightmargin=5pt,
innertopmargin=0pt,
leftmargin=0cm,
rightmargin=0cm,
linewidth=4pt,
innerbottommargin=0pt]{dBox}	

% Corollary box
\newmdenv[skipabove=7pt,
skipbelow=7pt,
rightline=false,
leftline=true,
topline=false,
bottomline=false,
linecolor=gray,
backgroundcolor=black!5,
innerleftmargin=5pt,
innerrightmargin=5pt,
innertopmargin=5pt,
leftmargin=0cm,
rightmargin=0cm,
linewidth=4pt,
innerbottommargin=5pt]{cBox}

% Creates an environment for each type of theorem and assigns it a theorem text style from the "Theorem Styles" section above and a colored box from above
\newenvironment{theorem}{\begin{tBox}\begin{theoremeT}}{\end{theoremeT}\end{tBox}}
\newenvironment{exercise}{\begin{eBox}\begin{exerciseT}}{\hfill{\color{accent}\tiny\ensuremath{\blacksquare}}\end{exerciseT}\end{eBox}}				  
\newenvironment{definition}{\begin{dBox}\begin{definitionT}}{\end{definitionT}\end{dBox}}	
\newenvironment{example}{\begin{exampleT}}{\hfill{\tiny\ensuremath{\blacksquare}}\end{exampleT}}		
\newenvironment{corollary}{\begin{cBox}\begin{corollaryT}}{\end{corollaryT}\end{cBox}}	

%----------------------------------------------------------------------------------------
%	REMARK ENVIRONMENT
%----------------------------------------------------------------------------------------

\newenvironment{remark}{\par\vspace{10pt}\small % Vertical white space above the remark and smaller font size
\begin{list}{}{
\leftmargin=35pt % Indentation on the left
\rightmargin=25pt}\item\ignorespaces % Indentation on the right
\makebox[-2.5pt]{\begin{tikzpicture}[overlay]
\node[draw=accent!60,line width=1pt,circle,font=\bfseries,inner sep=2pt,outer sep=0pt] at (-15pt,0pt){\textcolor{accent}{R}};\end{tikzpicture}} % Orange R in a circle
\advance\baselineskip -1pt}{\end{list}\vskip5pt} % Tighter line spacing and white space after remark