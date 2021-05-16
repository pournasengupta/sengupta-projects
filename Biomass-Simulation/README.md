\documentclass{article}



\usepackage{arxiv}

\usepackage[utf8]{inputenc} % allow utf-8 input
\usepackage[T1]{fontenc}    % use 8-bit T1 fonts
\usepackage{hyperref}       % hyperlinks
\usepackage{url}            % simple URL typesetting
\usepackage{booktabs}       % professional-quality tables
\usepackage{amsfonts}       % blackboard math symbols
\usepackage{nicefrac}       % compact symbols for 1/2, etc.
\usepackage{microtype}      % microtypography
\usepackage{lipsum}		% Can be removed after putting your text content
\usepackage{graphicx}
\usepackage[numbers]{natbib}
\usepackage{doi}
\usepackage{float}



\title{Simulating the Growth of Plants: A Simple Growth Model of Various Plants and the Effect of Environmental Factors}

%\date{September 9, 1985}	% Here you can change the date presented in the paper title
%\date{} 					% Or removing it

\author{ \href{https://orcid.org/0000-0000-0000-0000}{\includegraphics[scale=0.06]{orcid.pdf}\hspace{1mm}Ryan Goss} \\
	Department of Computer Science (CSCI 5314)\\
	University of Colorado\\
	Boulder, CO 80301 \\
	\texttt{ryan.goss@colorado.edu} \\
	%% examples of more authors
	\And
	\href{https://orcid.org/0000-0000-0000-0000}{\includegraphics[scale=0.06]{orcid.pdf}\hspace{1mm}Pourna Sengupta} \\
	Department of Computer Science (CSCI 4314)\\
	University of Colorado\\
	Boulder, CO 80301\\
	\texttt{pourna.sengupta@colorado.edu} \\
	%% \AND
	%% Coauthor \\
	%% Affiliation \\
	%% Address \\
	%% \texttt{email} \\
	%% \And
	%% Coauthor \\
	%% Affiliation \\
	%% Address \\
	%% \texttt{email} \\
	%% \And
	%% Coauthor \\
	%% Affiliation \\
	%% Address \\
	%% \texttt{email} \\
}

% Uncomment to remove the date
%\date{}

% Uncomment to override  the `A preprint' in the header
\renewcommand{\headeright}{Goss, R., Sengupta, P.}
% \renewcommand{\undertitle}{Technical Report}
\renewcommand{\shorttitle}{Simulating the Growth of Plants: A Simple Growth Model}

%%% Add PDF metadata to help others organize their library
%%% Once the PDF is generated, you can check the metadata with
%%% $ pdfinfo template.pdf
\hypersetup{
pdftitle={A template for the arxiv style},
pdfsubject={q-bio.NC, q-bio.QM},
pdfauthor={David S.~Hippocampus, Elias D.~Striatum},
pdfkeywords={First keyword, Second keyword, More},
}

\begin{document}
\maketitle

\begin{abstract}
A highly complex process in nature and the environment is the growth of plants and organic biomass. Understanding, simulating and predicting these processes as a confluence between biology and computer science has been a topic of intense research at least since the 1980s. This has spanned sub-fields of plant structural-functional modeling, plant-plant interactions to crop and macro-scale biomass prediction. Here, we present a simplified model for emulating the growth patterns of common greenhouse plants, accounting for environmental factors such as water and sunlight. Keeping sunlight distribution uniform throughout the greenhouse grid, we explore three different "greenhouse" watering scenarios containing up to three distinct plant species, each with their own water and sunlight sensitivity. With this framework, we show that a rudimentary simulation of plant growth (in terms of height and width) can be simulated and generally represents true-to-life plant growth behavior in response to these varying watering scenarios and plant presets (species).
\end{abstract}


% keywords can be removed
\keywords{plant growth \and computational modeling \and biomass simulation \and dynamic modeling of plants}


\section{Introduction}

A topic of intense study and interest in within the field of computational biological modeling is that of simulating the growth, structure and architecture of plants and biomass over time. While highly complex, such applications have been explored from a wide gamut of perspectives for the past decades. The topic areas receiving the most attention currently are perhaps structural architectural modeling of individual plant species (e.g., each anatomical stage of growth and corresponding physical structure), crop modeling to account for varying weather or environmental challenges and macro scale biomass modeling and prediction based on changing climate conditions, including in response to models of planetary climate change. Of course, while exploration is ongoing in many other related realms, we outline some of the previous related work in these topic areas, below.

\subsection{Modeling Individual Plant Growth Structure}

The field of individual plant structural growth modeling dates back several decades with aspirations of simulating each stage of plant growth and the associated behavior, structure and growth patterns. Given the breadth of the subject alone, the focus of such explorations have varied in terms of variables affecting growth (e.g., nutrients, oxygen/nitrogen levels, sunlight, plant species, cellular level modeling \citep{Meyer2014}) and approach (i.e., mathematical simulations \citep{Doak2005}, stochastic geometric growth modeling \citep{Kang2007} and machine learning approaches mimicking real plant growth utilizing computer vision techniques \citep{Lee2018}). 

Most notably, several software approaches have been developed over time to best approximate individual plant growth. The first such incarnation dates back approximately two decades with software called Atelier de Modelisation de 1'Architecture des Plantes (AMAP) which, in its early stages, was a rudimentary application for generating growth of various plants via some pre-programmed template controls while introducing some randomness to the model \citep{Jaeger1992}. From this platform, a more modern plan architectural and growth modeling software program has been developed, called GreenLab, derived from AMAP \citep{Cournede2005}. It was developed as part of a cross-functional collaboration of botonists, physiologists and mathematicians. A multitude of different plant species and parameters are available to model growth dynamics, including nutrient content, competition of resources, sunlight, etc with the ability to monitor output variables and visualize growth with computer graphics. Some examples of the types of structural plant modeling created with GreenLab is shown in Figure \ref{fig:examples}. 

\begin{figure}[h]
    \centering
    \includegraphics[width=16cm]{images/GLexamples.png}
    \caption{Examples of simulated structural plant growth, created with GreenLab. }
    \label{fig:examples}
\end{figure}

One such study utilizing GreenLab reported successful simulation of deterministic topological development of a Mongolian Scots pine species in its native habitat within a fragile and arid ecosystem. The authors observed accurate simulation of branching and growth patterns by using a stochastic functional-structural plant model in GreenLab 2 \citep{Wang2011}. The authors reported the method to be a successful technique to accurately model for charicterizing tree structure and biomass allocation, as shown in \ref{fig:wangresults}. A relatively recent publication argues that while the majority of plant modeling utilizes "process-based" modeling, which emulate factors contributing to growth, a "functional-structural plant model (FSPM)", like the Mongolian Scots pine model may be more flexible and definable with an ability to tweak factors ad hoc. Additionally, the authors, urge the need for a more generalizable FSPM that can be modularized and from a standard template for more efficient development \citep{Henke2016}.

\begin{figure}[h]
    \centering
    \includegraphics[width=16cm]{images/scots.png}
    \caption{Results from Wang et al. 2011, which modeled the growth of Mongolian Scots pine tree biomass and partitioning. "Fig 6" shows the continued modeled growth of trees at incremental ages. "Fig 4" graphs the branch and total biomass over aging of the tree. "Fig 5" shows the biomass of various tree organs from a monte carlo simulation (green lines are simulations, red line is average). }
    \label{fig:wangresults}
\end{figure}

\subsection{Crop Biomass Modeling}
A somewhat related popular research topic area to individual plant growth structural-functional modeling is that of crop or large-scale plant-matter modeling utilizing varying scales of geography. While the research realm deserves its own review paper, we provide a few recent primer examples. As accurate simulation of crop biomass holds promising applications ranging from yield prediction, planning for future food insecurities and deficits, optimization of farming practices, planning for catastrophic events and informing policy decisions, the field has seen significant attention dating back several decades, with some of the first usable and somewhat predictive models dating back to the mid 1980s \citep{liu2020}. 

One such example of an early simulation explored the modeling of the maize mono-crop by integrating two previously reported crop models to increase the real-world predictive biomass. The authors demonstrated that previously developed models (termed CERES, a miaze specific crop model and INTERCOM, a generic crop model used for miaze) underestimated the biomass yield from real-world measured crop growth and developed a novel model borrowing from the strengths of the two previous models. Specifically, it utilized a temperature-driven phenological development, canopy integration of photosynthesis assimilates and organ-specific growth and respiration. The model requires less hybrid crop parameters as in the CERES model yet is able to account for hybrid variations of miaze unlike the INTERCOM model. The authors demonstrated a dramatic improvement in crop biomass prediction using experimental results \citep{Yang2003}. 

\begin{figure}[htbp]
    \centering
    \includegraphics[width=16cm]{images/corn.png}
    \caption{Collection of spectra data with RedEye (left) and the APSIM biomass preditive mean (black) as compared to the measured value (green) from simulations of various locations (right) from \citep{Machwitz2014}. }
    \label{fig:biomass_corn}
\end{figure}

A more recent example of an approach to improve crop growth model accuracy was through the assimilation of satellite geospatial data. In an effort to improve the input parameters, so critical to the accurate prediction and modeling of crop growth models (CGM), researchers utilized a constellation of satellites (termed, "RedEye") to gather reflective spectra data and pigmentation data to be processed and interpreted to more accurately tweak input parameters. The updated input parameters are then delivered to the APSIM CGM to predict future biomass in the selected area. The authors determined a dramatic improvement in the predictive accuracy using this approach, indicating the utmost importance of correct input variables for modeling such a complex environmental process. Figure \ref{fig:biomass_corn} shows the collection of spectra data with RedEye (left) and the APSIM biomass predictive mean (black) as compared to the measured value (green) from simulations of various locations (right) \citep{Machwitz2014}. 

The importance of correct input variables was also emphasized in a recent publication demonstrating that collection of local survey data, such as planting time, climate conditions, fertilization, irrigation, etc. variables greatly enhances the predictive value for a CGM. Knowing and inputting these actual real-time variables were instrumental in significant increases in accuracy for forecasting biomass and food security of crop farms in Tanzania \citep{liu2020}. 

\begin{figure}[h]
    \centering
    \includegraphics[width=12cm]{images/tanzania.png}
    \caption{Process of field survey data collection and input to CGM (left) to improve biomass predictive accuracy with predicted vs. actual results (right) \citep{liu2020}. }
    \label{fig:tanzania}
\end{figure}

A very recent approach to improving CGM predictive accuracy, published in \emph{Nature} this year, utilized modern machine learning techniques coupled with crop modeling. The study utilized both APSIM CGM input parameters (i.e., yield, weather, soil, etc. data) and crop modeling output parameters (i.e., yield prediction, biomass prediction, water stress etc.) as input features for various machine learning models, including logistic regression, random forest, XGBoost etc. The authors were able to show a significant decrease in the root mean squared error (RMSE) for yield prediction and were able to isolate the most important input features for the ML models, with hydrological parameters being the most important \citep{Shahhosseini2021}. Figure \ref{ML} shows the improvements in RMSE when coupling ML techniques with crop growth models for predicting biomass yield.

\begin{figure}[h]
    \centering
    \includegraphics[width=10cm]{images/ML.png}
    \caption{Improvements in root mean squared error rates of baseline and ML-APSIM crop yield models, demonstrating significant improvements for all methods, with an ensemble approach yielding greatest reduction in error \citep{Shahhosseini2021}. }
    \label{fig:ML}
\end{figure}

\subsection{Our Project and Approach}
With a variety of perspectives and approaches within the broad field of plant, crop and biomass modeling, our investigation seeks to develop a relatively simple crop growth model on a somewhat small scale. We set out to develop a virtual \emph{greenhouse} to simulate a number of common vegetable, herb and/or house plants under varying environmental growing conditions. Given the time and resource constraints, our model is not intended to replicate the level of complexity and advancement as has been discussed (above) and previously published for either individual plant structural-functional simulation or crop yield prediction. Rather, the aim is to develop a somewhat simple, yet predictive, emulation of a plant growth environment, accounting primarily for plant watering and sunlight uptake variables. 

As such, the model developed here can allow for the creation of various virtual plant objects, which have their own representative properties such as color, growth rate, responsiveness to water and light. With this, virtual plants can be initialized as "seeds" either manually or randomly in positions throughout a Greenhouse area or "grid." By introducing simulated environmental factors such as water and sunlight at varying locations with gradating amounts throughout the Greenhouse area, the simulation can begin to predict rudimentary growth patterns of the plants, such as size, speed of growth. While the level of complexity for such a project can always be dramatically increased, i.e. to more accurately account for all environmental variables, plant-plant interactions and competition, soil properties, etc., the goal is to demonstrate a more proof of concept in a simplified, \emph{fun} and relatively easy to understand form. 

The focus of our model in this particular publication is to emulate and elucidate plant growth behaviour \emph{particularly with a focus on differing plant \textbf{watering patterns and differing plant species}}. In each case, we look to monitor plant size (height, width, biomass) as well as water needed to grow and water acquired from the environment. Specifically, we look at four distinct watering patterns: even distribution, sequential grid watering, downhill watering and random watering (primarily focusing on the first three). We run several simulations with varying numbers of plants constructed, evaluating up to a total of three distinct plant "species" generated (each with their own color, water sensitivity and light sensitivity). With the focus on watering patterns, our model assumes equal light distribution throughout each grid point in the greenhouse, yet, plants that grow faster (and therefore higher) receive a greater amount of light relative to other nearby plants, which further stimulates faster growth. 

\section{Methods}
To create the simplified crop growth model (CGM), a small python-based applet was created, represented at a high level in Figure \ref{fig:app}. For the simulation, a number of presets and global variables are hard coded in the \emph{run.py} file, including the greenhouse simulation size (height, length), number of timesteps to simulate, uniform water distributed, watering method as well as the number and "types" of plants to simulated. Plants are constructed using a Plant class, which specifies their location, appearance color, relative growth speed, water sensitivity (requirement) and status of growth (initiation, growing, wilting). \emph{Run.py} constructs a Greenhouse from the Greenhouse class, which initializes the greenhouse properties including grid size, water drain rate, timestep and all associated functions to carry out the simulation/animation. 
 
\begin{figure}[h]
    \centering
    \includegraphics[width=16cm]{images/app.png}
    \caption{A high level view of the plant growth simulation applet}
    \label{fig:app}
\end{figure}

\subsection{Key Simulation Functions and Parameters}
The key functions for the simulation are largely contained within the Greenhouse class. While there are a number of helper and utility functions, the critical methods for the simulation of the Greenhouse and plant growth are:
\begin{itemize}
    \item \emph{add\_plant}, which initializes the greenhouse grid with the plants;
    \item \emph{timeframe\_step}, which iterates through each frame of time, updates and calls the \emph{water\_plants} and \emph{grow\_plants} functions;
    \item \emph{water\_plants} function updates the greenhouse grid with water amounts from the type of watering method used (random or downhill);
    \item \emph{uptake\_water} function sends nearby water to each nearby plant. Higher water sensitive plants will not uptake as much water as more water "thirsty" plants (specified by the "w\_effect" plant parameter);
    \item \emph{add\_sunlight} adds a sunlight particle to each nearby (defined as a set local distance) tallest plant. The sunlgiht particle acts as a multiplier for the "l\_effect" plant parameter, discussed below;
    \item \emph{grow\_plants} iterates through each plant and adds to each plant size (height and width) by multiplying the "w\_effect" variable by the amount of nearby water ("water\_amount")
\end{itemize}

In terms of how the simulation is created, each constructed plant is initialized with its own key parameters of \emph{color}, \emph{w\_effect}, which controls the sensitivity to nearby water and thereby growth speed and \emph{l\_effect}, which controls how sensitive the plant is to uniform sun particles. The \emph{w\_effect} parameter and \emph{l\_effect} parameters collectively control how fast a plant will grow in the presence of nearby (required) water. The \emph{w\_effect} controls how rapidly the plant will uptake water from its surrounding environment. The amount of water taken up will subtract that amount nearby, limiting the amount available to surrounding plants as well as contribute to the amount a plant can grow. The \emph{l\_effect} acts as a multiplier for plants that grow higher faster. That is, in this model, light is considered equally distributed with each greenhouse grid point having its own and equal amount of light (one light particle per grid square) with tallest plants in a local minimum receiving the most light, acting as a multiplier to growth speed. This reinforces the growth rate of taller local plants. 

Therefore, the relatively simple equation by which plant growth (height and width) is calculated each timeframe is shown below with the following variables:
\begin{itemize}
    \item \emph{light\_amount} - plant class property that adds light amount if plant is tallest nearby plant. The wider the plant is, the more light will also be absorbed since light is absorbed by greenhouse grid squares plant encompasses.
    \item \emph{water\_amount} - plant class property that absorbs water based on the nearby water that has been distributed in the greenhouse grid.
    \item \emph{w\_effect} - plant preset acting as multiplier on growth given amount of water absorbed.
    \item \emph{l\_effect} - plant preset acting as a multiplier on the amount of sunlight absorbed. The amount of sunlight that is absorbed increases the max amount of water a given plant can absorb. The more water a plant can absorb, the faster it can grow.
\end{itemize}

\begin{equation}
    \textbf{growth\_width} = (\emph{w\_effect} * \emph{plant.water\_amount}) * (light\_amount / plant.num\_gridpoints)
\end{equation}

\begin{equation}
    \textbf{growth\_height} = (\emph{w\_effect} * \emph{plant.water\_amount}) * (1 - (light\_amount / plant.num\_gridpoints))
\end{equation}

As the plants increase in height, the tallest nearby plants absorb the greatest amount of sunlight, which increases the max amount of water a given plant can absorb. Once water is distributed to nearby grid points, the plants uptake the water, which is used to grow the plant in an x and y simulated direction. As shown in equation (1), the growth height depends on the \emph{w\_effect} preset, plant \emph{water\_amount} absorbed and the ratio of the \emph{light\_amount} to amount of plant gridpoints covered. The height depends on the inverse of this \emph{light\_amount} ratio.

\subsection{Simulated Plant Type Sets}
The simulation was tested using a variety of plant type sets that included combinations of tomato, lettuce, corn, basil and thyme plants (hypothetical plant types, each with their own color, light and water sensitivity). Characteristics of each plant species was adjusted to realistic parameters for testing. Each set was simulated under three watering procedures and factors of plant height, radius, water absorption, and water requirements were plotted using the simulation. Three sets \ref{fig:sets} are presented here as examples of the model performance.

\begin{figure}[h]
    \centering
    \includegraphics[width=16cm]{images/sets.png}
    \caption{Sample of Plant Type Sets from Simulated Sets. Each plant has its own unique input parameters. In order, they are: color (rgb setting), \emph{w\_effect} param, \emph{l\_effect} param and plant name}
    \label{fig:sets}
\end{figure}
\clearpage

\section{Results}
The results from four different simulations are presented below. Each simulation was ran with a uniform, sequential and downhill watering pattern. The sequential watering pattern distributes water stepwise in grid partitions with the downhill pattern distributing water more densely at the top of the greenhouse grid (simulating lower elevation). A simulation base case contains a single plant of each type from \emph{set1} while the simulations for \emph{set1}, \emph{set2} and \emph{set3} contain at least 50 plants per species.

When interpreting the following figures, the animation snapshots, shown in Figures \ref{fig:base1}, \ref{fig:base2}, \ref{fig:base3}, \ref{fig:set1}, \ref{fig:set2} and \ref{fig:set3} are of the final timepoint in the simulation, showing the final plant size. Water is represented as shades of blue, with darker hues representing a greater amount of water density. As is quite apparent, in many of the simulations we had instances where certain individual plants or plant species overgrew the greenhouse, covering the entire area. Each simulation was run for a total of 100 time frames.

\subsection{Simulation Base Cases}
\begin{figure}[h]
    \centering
    \includegraphics[width=6.5cm]{basecase/sim1u.png}
    \includegraphics[width=6.5cm]{basecase/sim1s.png}
    \includegraphics[width=6.5cm]{basecase/sim1d.png}
    \caption{Set 1 Uniform|Sequential|Downhill Simulation}
    \label{fig:base1}
\end{figure}

\clearpage

\subsection{Simulations of Differing Watering Patterns}
\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/sim1u.png}
    \includegraphics[width=5.25cm]{results/sim1s.png}
    \includegraphics[width=5.25cm]{results/sim1d.png}
    \caption{Set 1 Uniform|Sequential|Downhill Simulation}
    \label{fig:set1}
\end{figure}


\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/sim2u.png}
    \includegraphics[width=5.25cm]{results/sim2s.png}
    \includegraphics[width=5.25cm]{results/sim2d.png}
    \caption{Set 2 Uniform|Sequential|Downhill Simulation}
    \label{fig:set2}
\end{figure}

\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/sim3u.png}
    \includegraphics[width=5.25cm]{results/sim3s.png}
    \includegraphics[width=5.25cm]{results/sim3d.png}
    \caption{Set 3 Uniform|Sequential|Downhill Simulation}
    \label{fig:set3}
\end{figure}

\clearpage
\subsection{Set 1 Simulated Factors}
\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/height1u.png}
    \includegraphics[width=5.25cm]{results/height1s.png}
    \includegraphics[width=5.25cm]{results/height1d.png}
    \caption{Set 1 Uniform|Sequential|Downhill Height}
    \label{fig:set1h}
\end{figure}

\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/rad1u.png}
    \includegraphics[width=5.25cm]{results/rad1s.png}
    \includegraphics[width=5.25cm]{results/rad1d.png}
    \caption{Set 1 Uniform|Sequential|Downhill Radius}
    \label{fig:set1r}
\end{figure}

\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/wa1u.png}
    \includegraphics[width=5.25cm]{results/wa1s.png}
    \includegraphics[width=5.25cm]{results/wa1d.png}
    \caption{Set 1 Uniform|Sequential|Downhill Water Absorption}
    \label{fig:set1wa}
\end{figure}
\clearpage
\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/wr1u.png}
    \includegraphics[width=5.25cm]{results/wr1s.png}
    \includegraphics[width=5.25cm]{results/wr1d.png}
    \caption{Set 1 Uniform|Sequential|Downhill Water Requirement}
    \label{fig:set1wr}
\end{figure}




\subsection{Set 2 Simulated Factors}
\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/height2u.png}
    \includegraphics[width=5.25cm]{results/height2s.png}
    \includegraphics[width=5.25cm]{results/height2d.png}
    \caption{Set 2 Uniform|Sequential|Downhill Height}
    \label{fig:set2h}
\end{figure}

\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/radu2.png}
    \includegraphics[width=5.25cm]{results/rad2s.png}
    \includegraphics[width=5.25cm]{results/rad2d.png}
    \caption{Set 2 Uniform|Sequential|Downhill Radius}
    \label{fig:set2r}
\end{figure}
\clearpage
\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/wa2u.png}
    \includegraphics[width=5.25cm]{results/wa2s.png}
    \includegraphics[width=5.25cm]{results/wa2d.png}
    \caption{Set 2 Uniform|Sequential|Downhill Water Absorption}
    \label{fig:set2wa}
\end{figure}

\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/wr2u.png}
    \includegraphics[width=5.25cm]{results/wr2s.png}
    \includegraphics[width=5.25cm]{results/wr2d.png}
    \caption{Set 2 Uniform|Sequential|Downhill Water Requirement}
    \label{fig:set2wr}
\end{figure}




\subsection{Set 3 Simulated Factors}
\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/height3u.png}
    \includegraphics[width=5.25cm]{results/height3s.png}
    \includegraphics[width=5.25cm]{results/height3d.png}
    \caption{Set 3 Uniform|Sequential|Downhill Height}
    \label{fig:set3h}
\end{figure}

\clearpage
\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/rad3u.png}
    \includegraphics[width=5.25cm]{results/rad3s.png}
    \includegraphics[width=5.25cm]{results/rad3d.png}
    \caption{Set 3 Uniform|Sequential|Downhill Radius}
    \label{fig:set3r}
\end{figure}

\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/wa3u.png}
    \includegraphics[width=5.25cm]{results/wa3s.png}
    \includegraphics[width=5.25cm]{results/wa3d.png}
    \caption{Set 3 Uniform|Sequential|Downhill Water Absorption}
    \label{fig:set3wa}
\end{figure}

\begin{figure}[h]
    \centering
    \includegraphics[width=5.25cm]{results/wr3u.png}
    \includegraphics[width=5.25cm]{results/wr3s.png}
    \includegraphics[width=5.25cm]{results/wr3d.png}
    \caption{Set 1 Uniform|Sequential|Downhill Water Requirement}
    \label{fig:set3wr}
\end{figure}

% \begin{table}
% 	\caption{Sample table title}
% 	\centering
% 	\begin{tabular}{ll}
% 		\toprule
% 		\multicolumn{2}{c}{Part}                   \\
% 		\cmidrule(r){1-2}
% 		Name     & Description     & Size ($\mu$m) \\
% 		\midrule
% 		Dendrite & Input terminal  & $\sim$100     \\
% 		Axon     & Output terminal & $\sim$10      \\
% 		Soma     & Cell body       & up to $10^6$  \\
% 		\bottomrule
% 	\end{tabular}
% 	\label{tab:table}
% \end{table}

% \subsection{Lists}
% \begin{itemize}
% 	\item Lorem ipsum dolor sit amet
% 	\item consectetur adipiscing elit.
% 	\item Aliquam dignissim blandit est, in dictum tortor gravida eget. In ac rutrum magna.
% \end{itemize}

\section{Discussion}
Overall, the developed model did produce a somewhat realistic simulation of plant growth behavior in response to local water amounts and evenly distributed sunlight. By looking at three distinct watering patterns, we were able to evaluate 1) the effect simulated water has on plant growth and 2) whether the simulated behavior is close to biological plant growth. 

Plants with an increased sensitivity to water and light (\emph{w\_effect} and \emph{l\_effect}) grew at much higher rates when provided with required water levels or placed in a runoff location. It is clearly observed from the animations and final plant states that plants within an area of high water density dramatically benefited and grew much faster. 

The simulation also shows that all three species of plants overall grow better when downhill irrigation is used. Uniform irrigation of plants typically results in the overgrowth of a more dominant species. Sequential irrigation resulted in limited growth, with all species growing equally, but very slowly. Downhill irrigation, combining a uniform and sequential irrigation system produced biomass growth that was most ideal for all three species. All species in set 1 were able to access the necessary resources for growth and competition was reduced when possible. 

By watering plants downhill, the plants located at higher elevations grew at a decreased rate than those placed lower. Water runoff proved to be a very valuable resource to plants located downhill and greatly aided in the growth process of all species. Unlike set 1, set 3 showed an excessive overgrowth of one species when using downhill irrigation. This species, originally located downhill, was able to take over the majority of area sampled due to the excessive resources received. Plants originally located at higher elevations not only are deprived of water due to runoff, but also easily die off as a result of lack of nutrients and provide no competition to the overgrowing species. 

\section{Conclusion}
The simulation proved capable of expecting impact of resources on plant growth and including considerations based on environment and other factors. Though only a few factors were testing in the early versions of this simulation, future work is capable of including a multitude of resources and growth factors. The inclusion of weather, sunshine, or human/animal impact on plant growth can aid in making the simulation a tool for many scientists, researchers, and even those simply planting a garden in their yard. 

Considering differing environments such as forests, rain forests, desserts, parks, and cities allow for factors such as pollution, construction, climate change to be included. These factors mirror those of the real-world and allow for a realistic simulation that can help predict levels of $CO_2:O$ production ratios between animals and plants. 

Overall, the simulation has great potential to be an incredibly useful and efficient tool that can be implemented in many ways. Understanding our environment and working to better provide and care for it is a crucial part of humanities survival. Simulations, such as this, can be used not only for predicting plant growth in greenhouses or on farm land but to also predict the impact of human interactions on plant growth. 

\section{Contributions}


\bibliographystyle{unsrtnat}
\bibliography{references}  %%% Uncomment this line and comment out the ``thebibliography'' section below to use the external .bib file (using bibtex) .


%%% Uncomment this section and comment out the \bibliography{references} line above to use inline references.
% \begin{thebibliography}{1}

% 	\bibitem{kour2014real}
% 	George Kour and Raid Saabne.
% 	\newblock Real-time segmentation of on-line handwritten arabic script.
% 	\newblock In {\em Frontiers in Handwriting Recognition (ICFHR), 2014 14th
% 			International Conference on}, pages 417--422. IEEE, 2014.

% 	\bibitem{kour2014fast}
% 	George Kour and Raid Saabne.
% 	\newblock Fast classification of handwritten on-line arabic characters.
% 	\newblock In {\em Soft Computing and Pattern Recognition (SoCPaR), 2014 6th
% 			International Conference of}, pages 312--318. IEEE, 2014.

% 	\bibitem{hadash2018estimate}
% 	Guy Hadash, Einat Kermany, Boaz Carmeli, Ofer Lavi, George Kour, and Alon
% 	Jacovi.
% 	\newblock Estimate and replace: A novel approach to integrating deep neural
% 	networks with existing applications.
% 	\newblock {\em arXiv preprint arXiv:1804.09028}, 2018.

% \end{thebibliography}


\end{document}
