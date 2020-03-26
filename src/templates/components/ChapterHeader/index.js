import React from 'react';
import { FaChevronLeft } from 'react-icons/fa';
import { navigate } from 'gatsby';
import { Header, BackLink, LessonTitle, HelpButton } from './styled';
function ChapterHeader() {
  return (
    <Header>
      <BackLink onClick={() => navigate('/')}>
        <FaChevronLeft size={30} />
      </BackLink>
      <LessonTitle>Lesson: Introduction to Smartpy</LessonTitle>
      <HelpButton>Get Help</HelpButton>
    </Header>
  );
}

export default ChapterHeader;
