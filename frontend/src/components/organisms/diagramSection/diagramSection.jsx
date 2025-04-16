import React from 'react'
import mermaid from 'mermaid'
import svgPanZoom from 'svg-pan-zoom';

const styles = {
    display: 'flex',
    justifyContent: 'center'
}

export default class DiagramSectionComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            mermaidError: null
        };
    }
    
    componentDidMount() {
        mermaid.initialize({
            startOnLoad: true
        });
        mermaid.contentLoaded();
    
        mermaid.parseError = (error, hash) => {
            console.error('Mermaid errors:', error);
            this.setState({ mermaidError: error.str });
        };
    }
    
    componentDidUpdate(prevProps) {
        mermaid.contentLoaded();

        if (prevProps.chart !== this.props.chart) {
            const mermaidgraph = document.getElementById('mermaid-chart');
            if (mermaidgraph) {
                mermaidgraph.removeAttribute('data-processed');
            }
            this.handleDiagramCodeChange(this.props.chart);

            setTimeout(() => {
                const element = document.querySelector('.mermaid').querySelector('svg');
                const elementId = element.getAttribute('id');
                window.zoomTiger = svgPanZoom(`#${elementId}`, {
                    zoomEnabled: true,
                    controlIconsEnabled: true,
                    fit: true,
                    center: true,
                });
            }, 1000);
        }
    }

    handleDiagramCodeChange = async (newDiagramCode) => {
        try {
            const isValidSyntax = await mermaid.parse(newDiagramCode);
            if (isValidSyntax) {
                this.setState({ mermaidError: null });
            } else {
                this.setState({ mermaidError: mermaid.parseError });
            }
        } catch (error) {
            console.error('Ошибка при построении диаграммы:', error);
            this.setState({mermaidError: error.message});
        }
    };

    render() {
        if (!this.props.chart) {
            console.log(this.props.chart)
            return (<div style={styles} id="mermaid-chart" className="mermaid">
                {this.state.mermaidError ?
                (<div style={{ color: 'white' }}></div>) :
                ('flowchart TD\n')}
            </div>)
        }

        console.log(this.props.chart)
        return (
            <div style={styles} id="mermaid-chart" className="mermaid">
                {this.state.mermaidError ?
                (<div style={{ color: 'white' }}></div>) :
                (this.props.chart)}
            </div>
        );
    }
}
