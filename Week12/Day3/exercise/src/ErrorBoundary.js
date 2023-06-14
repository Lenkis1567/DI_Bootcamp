import React from 'react';

class ErrorBoundary extends React.Component {
    constructor() {
        super();
        this.state = {
            hasError: false,
            error:null,
            errorInfo:null,
        }
    }
    componentDidCatch(error, errorInfo) {
        console.log('error=>', error)
        console.log('errorInfo=>', errorInfo)
        this.setState({
            hasError:true, 
            error: error, 
            errorInfo: errorInfo}) //write to a log file
    }

    render() {
        if (this.state.hasError) {
            return (
                <div>
                    
                    {this.state.error.message}
                    <br />
                <details style={{ whiteSpace: 'pre-wrap' }}>
                    {this.state.error && this.state.error.toString()}
                     <br />
                     {this.state.errorInfo.componentStack}
                </details>
                </div>
            )
        }
        return this.props.children
    }
}

export default ErrorBoundary