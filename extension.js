const vscode = require('vscode');
const axios = require('axios');

function activate(context) {
    console.log('DeepSeek Code Assistant is now active!');


    let suggestCodeDisposable = vscode.commands.registerCommand('deepseek.suggestCode', async function () {
        const editor = vscode.window.activeTextEditor;
        if (editor) {
            const selection = editor.selection;
            const selectedText = editor.document.getText(selection);

            if (!selectedText) {
                vscode.window.showErrorMessage('No text selected. Please select some code to get suggestions.');
                return;
            }

            try {
                const response = await axios.post('http://localhost:5000/suggest', {
                    code: selectedText
                });

                const suggestion = response.data.suggestion;

                
                editor.edit(editBuilder => {
                    editBuilder.replace(selection, suggestion);
                });

                vscode.window.showInformationMessage('Code suggestion applied!');
            } catch (error) {
                vscode.window.showErrorMessage('Failed to fetch code suggestion. Please check the server.');
                console.error(error);
            }
        }
    });

    let detectErrorsDisposable = vscode.commands.registerCommand('deepseek.detectErrors', async function () {
        const editor = vscode.window.activeTextEditor;
        if (editor) {
            const selection = editor.selection;
            const selectedText = editor.document.getText(selection);

            if (!selectedText) {
                vscode.window.showErrorMessage('No text selected. Please select some code to detect errors.');
                return;
            }

            try {
                const response = await axios.post('http://localhost:5000/detect-errors', {
                    code: selectedText
                });

                const errors = response.data.errors;

             
                const outputChannel = vscode.window.createOutputChannel('DeepSeek Error Detection');
                outputChannel.clear();
                outputChannel.appendLine("Errors detected:");
                outputChannel.appendLine(errors);
                outputChannel.show(true);

            } catch (error) {
                vscode.window.showErrorMessage('Failed to detect errors. Please check the server.');
                console.error(error);
            }
        }
    });

    let refactorCodeDisposable = vscode.commands.registerCommand('deepseek.refactorCode', async function () {
        const editor = vscode.window.activeTextEditor;
        if (editor) {
            const selection = editor.selection;
            const selectedText = editor.document.getText(selection);

            if (!selectedText) {
                vscode.window.showErrorMessage('No text selected. Please select some code to refactor.');
                return;
            }

            try {
                const response = await axios.post('http://localhost:5000/refactor', {
                    code: selectedText
                });

                const refactoredCode = response.data.refactoredCode;

               
                editor.edit(editBuilder => {
                    editBuilder.replace(selection, refactoredCode);
                });

                vscode.window.showInformationMessage('Code refactored successfully!');
            } catch (error) {
                vscode.window.showErrorMessage('Failed to refactor code. Please check the server.');
                console.error(error);
            }
        }
    });


    let summarizeCodeDisposable = vscode.commands.registerCommand('deepseek.summarizeCode', async function () {
        const editor = vscode.window.activeTextEditor;
        if (editor) {
            const selection = editor.selection;
            const selectedText = editor.document.getText(selection);

            if (!selectedText) {
                vscode.window.showErrorMessage('No text selected. Please select some code to summarize.');
                return;
            }

            try {
                const response = await axios.post('http://localhost:5000/summarize', {
                    code: selectedText
                });

                const summary = response.data.summary;

    
                const outputChannel = vscode.window.createOutputChannel('DeepSeek Code Summary');
                outputChannel.clear();
                outputChannel.appendLine("Code Summary:");
                outputChannel.appendLine(summary);
                outputChannel.show(true);

            } catch (error) {
                vscode.window.showErrorMessage('Failed to summarize code. Please check the server.');
                console.error(error);
            }
        }
    });


    context.subscriptions.push(
        suggestCodeDisposable,
        detectErrorsDisposable,
        refactorCodeDisposable,
        summarizeCodeDisposable
    );
}

function deactivate() {
    console.log('DeepSeek Code Assistant is now deactivated.');
}

module.exports = {
    activate,
    deactivate
};