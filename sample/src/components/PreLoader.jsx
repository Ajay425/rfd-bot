import { useEffect } from 'react';
import './Preloader.css';
import { preLoaderAnim } from '../animations';

const PreLoader = () => {
  useEffect(() => {
    preLoaderAnim();
  }, []);

  return (
    <div className='preLoader'>
      <div className='texts-container'>
        <span>Welcome</span> 
        <span>to</span>
        <span>Trackmysubs</span>
      </div>
    </div>
  );
};

export default PreLoader;
