\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cslessonsolutions}
\LoadClass{article}

\RequirePackage[dvips,letterpaper,margin=1in,bottom=0.7in]{geometry}
\RequirePackage{helvet}
\RequirePackage{titlesec}
\RequirePackage{enumitem}
\RequirePackage[fleqn]{amsmath}

\let\@lessonnum\@empty
\newcommand{\lessonnum}[1]{\gdef\@lessonnum{#1}}

\titleformat{\section}
  {\normalfont\sffamily\Large\bfseries}
  {\thesection}{1em}{}
  
\renewcommand{\maketitle}{
    \section*{Solutions}
    {\large\textit{Lesson {\@lessonnum}: \@title}}
    \vspace{1ex}\hrule
}