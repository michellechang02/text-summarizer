import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'
import { ChakraProvider, VStack, Card, CardHeader, Heading, Textarea, Flex, HStack, Button, useClipboard, Spacer} from '@chakra-ui/react'
import {FilePlus, Clipboard} from 'react-feather'

function App() {
  let [value, setValue] = useState('')
  let [summary, setSummary] = useState('')
  const { hasCopied, onCopy } = useClipboard(summary);

  const summarizeText = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/summarize', {
        text: value,
      });

      if (response.status === 200) {
        setSummary(response.data.summary);
      } else {
        console.error('Failed to summarize text');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  useEffect(() => {

  }, [summary])



  return (
    <ChakraProvider>
      <Flex height="100vh" alignItems="center" justifyContent="center">
      <VStack spacing={20} align="stretch" width="80vw">
        <Card maxW="80vw" p={4}>
          
          <CardHeader>
            <HStack>
            <Heading size='md'>Initial Text</Heading>
            <Button ml={5} onClick={summarizeText}>
            <HStack spacing={2}>
            <span>Summarize</span>
            <FilePlus />
          </HStack>
            </Button>
            
            </HStack>
          </CardHeader>
          <Textarea
            value={value}
            onChange={(e) => setValue(e.target.value)}
            placeholder="Enter text to summarize here"
            size="sm"
           
          />
        </Card>
        <Card maxW="80vw" p={4}>
          <CardHeader>
          <HStack>
            <Heading size='md'>Summarized Text</Heading>
            <Button ml={5} onClick={onCopy}>
          <HStack spacing={2}>
            <span>{hasCopied ? 'Copied' : 'Copy'}</span>
            <Clipboard />
          </HStack>
        </Button>
            </HStack>
          </CardHeader>
          <Textarea
            value={summary}
            isReadOnly
            placeholder="Summarized text will appear here"
            size="sm"
           
          />
        </Card>
      </VStack>
    </Flex>
    </ChakraProvider>
  )
}

export default App
